from __future__ import annotations

import ast
import json
import random
import re
import subprocess
import sys
import tempfile
import textwrap
import time
from pathlib import Path

import torch
from datasets import load_from_disk
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

import count_assert
import utils


def fetch_data(dataset_path, sample_size=949):
    ds = load_from_disk(dataset_path)
    
    id_list = ds["train"]["in_source_id"]
    prompt_list = ds["train"]["problem"]
    test_list = ds["train"]["verification_info"]
    
    store = []
    total_num = len(id_list)
    for i in tqdm(range(total_num), desc="Reading the dataset"):
        temp_list = [id_list[i], prompt_list[i], test_list[i]['test_cases']]
        store.append(temp_list)
    
    #store = random.sample(store, sample_size)
    return store

def generate_python_file(testset, model_id, cache_dir, each_num):

    tokenizer = AutoTokenizer.from_pretrained(
        model_id,
        cache_dir=cache_dir,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        cache_dir=cache_dir,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
    )
    
    total_len = len(testset)
    conf_dict = {}
    for i in tqdm(range(total_len), desc="processing"):
        after_num = 0
        for j in range(each_num):
            current_case = testset[i]
            prompt = current_case[1]
            
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an expert competitive programmer.\n"
                        "Output ONLY valid Python code. No markdown, no backticks, no explanations, no extra text.\n"
                        "Do all reasoning silently.\n"
                    )
                },
                {
                    "role": "user",
                    "content": (
                        "Write a complete Python program that solves the following problem.\n\n"
                        "Hard requirements:\n"
                        "- Read from stdin, write to stdout.\n"
                        "- Implement solve() and call it in: if __name__ == '__main__': solve()\n"
                        "- Use fast I/O (sys.stdin.buffer.read).\n"
                        "- Follow the exact output format in the statement.\n"
                        "- With correct intendation.\n"
                        "- Handle edge cases.\n\n"
                        "PROBLEM:\n"
                        f"{prompt}\n"
                    )
                },
                        ]

            inputs = tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
                enable_thinking=False
            ).to(model.device)

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=2000,
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.9,
                )

            generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
            raw_resp = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
            
            # temp_lines = current_case[1].splitlines()
            # import_line = '\n'
            # for line in temp_lines:
            #     if 'import' in line:
            #         import_line += line + '\n'
            # raw_resp = "\n".join('    ' + line for line in raw_resp.splitlines())
            
            # base_code = current_case[2] + '\n\n' + import_line + raw_resp
            
            # base_code = current_case[2] + '\n\n' + raw_resp
            # ast_work = 0
            # try:
            #     test_func_name = utils.extract_func_name(raw_resp)
            # except SyntaxError:
            #     ast_work = 1
            #     pass
            # except IndentationError:
            #     ast_work = 1
            #     pass
            # if ast_work == 1:
            #     re_mod = re.compile(r'^\s*(?:async\s+)?def\s+([A-Za-z_]\w*)\s*\(', re.M)
            #     code = strip_code_fences(raw_resp)
            #     m = re_mod.search(code)
            #     if m:
            #         test_func_name = m.group(1)
            #     else:
            #         test_func_name = None
            
            # test_code = '\n\ncheck(' + test_func_name[-1] + ')'
            # base_code += test_code
            
            python_file_name = 'verifiable_coding_' + str(current_case[0]) + '_' + str(after_num) + '.py'
            python_file_name = re.sub(r'/', '_', python_file_name)
            test_key = python_file_name
            python_file_name = 'verifiable_coding/' + python_file_name
            with open(python_file_name, 'w') as f:
                f.write(raw_resp)
            after_num += 1
            
            messages = [
                {"role":"user","content": """Here is the python code you generated: """ + raw_resp + """
Here is the task requirement: """ + prompt + """

Give me your confidence level for your code.

Requirements:
- Output ONLY confidence level. No markdown, no explanations.
- The confidence level is between 0 to 1, which is a float.
"""}
                        ]
            
            inputs = tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
                enable_thinking=False
            ).to(model.device)

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=2048,  
                    do_sample=False,
                )

            generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
            raw_resp = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
            
            the_conf = float(raw_resp)
            conf_dict[test_key] = the_conf
            
    return conf_dict

def test_current_py_code(the_dataset, repeat_num, folder, pattern): 
    test_dict = {}
    for data in the_dataset:
        after_num = 0
        for i in range(repeat_num):
            python_file_name = 'verifiable_coding_' + str(data[0]) + '_' + str(after_num) + '.py'
            after_num += 1
            test_dict[python_file_name] = data[2]
    # print(test_dict['verifiable_coding_0_0.py'][0]['input'])
    
    folder = Path(folder)
    python_exe = sys.executable
    
    files = sorted(folder.rglob(pattern), key=utils.verifiable_coding_id)
    if not files:
        print(f"No files matched: {folder} / {pattern}")
        return 0
    
    ok, failed = 0, 0
    results = []
    count_dict = {}
    
    for i in tqdm(range(len(files)), desc="Testing Generated Code"):
        f = files[i]
        path_name_list = str(f).split('/')
        store_name = path_name_list[1]
        #store_name = utils.key_name_update(key_name)
        stdin_text_list = test_dict[store_name]
        
        success = 0
        base = 0
        passed = 0
        for stdin_text_base in stdin_text_list:
            stdin_text = stdin_text_base['input']
            std_out_true = stdin_text_base['output']
            
            timedout = 0
            try:
                proc = subprocess.run(
                    [python_exe, str(f)],
                    input=stdin_text,
                    capture_output=True,
                    text=True,
                    timeout=20,
                )
            except subprocess.TimeoutExpired as e:
                proc = None
                timedout = 1
            
            base += 1
            if timedout == 0:
                if proc.stdout == std_out_true:
                    success += 1
                    passed = 1
                    
        if store_name not in count_dict.keys():
            count_dict[store_name] = []
        
        count_dict[store_name].append(success)
        count_dict[store_name].append(base)
            
        if passed:
            ok += 1
        else:
            failed += 1
            
    print(f"Done. PASS={ok}, FAIL={failed}, TOTAL={len(files)}")

    return count_dict

if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/verifiable_coding_problems_python"
    sample_size = 949
    the_dataset = fetch_data(dataset_path, sample_size)

    model_id = "Qwen/Qwen3-4B"
    cache_dir = "/data/ruoyu/model"
    repeat_num = 1
    the_conf = generate_python_file(the_dataset, model_id, cache_dir, repeat_num)
    
    out_dict = test_current_py_code(the_dataset, 1, "./verifiable_coding", "*.py")
    print(out_dict)
    utils.creat_json_for_eval(out_dict, 'verifiable_out', the_conf)