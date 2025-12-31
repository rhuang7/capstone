from __future__ import annotations
import subprocess
import sys
from pathlib import Path
from datasets import load_from_disk
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
import random
import re
import time
import utils
import ast
import count_assert


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
    test_dict = {}
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
            
            test_dict[test_key] = current_case[2]
            
    return test_dict

def test_current_py_code(the_dataset): 
    print(type(the_dataset))
    return

if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/verifiable_coding_problems_python"
    sample_size = 949
    the_dataset = fetch_data(dataset_path, sample_size)

    # model_id = "Qwen/Qwen3-4B"
    # cache_dir = "/data/ruoyu/model"
    # repeat_num = 1
    # test_dict = generate_python_file(the_dataset, model_id, cache_dir, repeat_num)
    
    test_current_py_code(the_dataset)