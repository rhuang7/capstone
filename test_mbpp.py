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

def func_name_after_assert(line: str) -> str | None:
    node = ast.parse(line).body[0]          # should be an ast.Assert
    if not isinstance(node, ast.Assert):
        return None

    # assert <left> == <right>
    test = node.test
    if not (isinstance(test, ast.Compare) and len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq)):
        return None

    left = test.left                        # should be a Call: min_cost(...)
    if not isinstance(left, ast.Call):
        return None

    f = left.func                           # could be Name or Attribute (obj.min_cost)
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return None

def covert_testlist_in_func(the_list):
    test_func = 'def check(candidate):\n'
    for line in the_list:
        test_name = func_name_after_assert(line)
        line = line.replace(test_name, "candidate")
        test_func += '    ' + line + '\n'
    
    return test_func
    

def fetch_data(dataset_path, sample_size=974):
    ds = load_from_disk(dataset_path)
    
    id_list = ds["test"]["task_id"]
    prompt_list = ds["test"]["text"]
    test_list = ds["test"]["test_list"]
    
    store = []
    total_num = len(id_list)
    for i in tqdm(range(total_num), desc="Reading the dataset"):
        temp_list = [id_list[i], prompt_list[i], covert_testlist_in_func(test_list[i])]
        store.append(temp_list)
    
    #store = random.sample(store, sample_size)
    return store[:2]

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
    for i in tqdm(range(total_len), desc="processing"):
        after_num = 0
        for j in range(each_num):
            current_case = testset[i]
            prompt = current_case[1]
            
            messages = [
                {"role":"system","content":"You are a code completion model. Output ONLY the function define and function body. The code MUST be complete and executable. Do not stop early."},
                {"role":"user","content": """You are given a programming prompt that already contains any required imports, the target function signature, and its docstring.

Your task:
1) Copy the entire prompt block below into your output EXACTLY as-is (character-for-character). Do not change imports, the def line, indentation, or the docstring.
2) Then, COMPLETE the function body so that it correctly solves the task described by the docstring.
3) You may add helper code ONLY if needed, but do NOT rename, remove, or alter the target function signature.
4) Output a single, complete, runnable Python file. Output ONLY Python code and nothing else.
5) Import any libraries you used in your answer.

PROMPT (copy this verbatim into your output, then fill in the function body):
<<<PROMPT
""" + prompt + """
PROMPT>>>"""}
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
            temp_lines = current_case[1].splitlines()
            import_line = '\n'
            for line in temp_lines:
                if 'import' in line:
                    import_line += line + '\n'
            # raw_resp = "\n".join('    ' + line for line in raw_resp.splitlines())
            
            base_code = current_case[2] + '\n\n' + import_line + raw_resp
            test_func_name = utils.extract_func_name(current_case[1])
            test_code = '\n\ncheck(' + test_func_name[-1] + ')'
            base_code += test_code
            
            python_file_name = current_case[0] + '_' + str(after_num) + '.py'
            python_file_name = re.sub(r'/', '_', python_file_name)
            python_file_name = 'mbpp/' + python_file_name
            with open(python_file_name, 'w') as f:
                f.write(base_code)
            after_num += 1
            
    return


if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/mbpp"
    sample_size = 974
    the_dataset = fetch_data(dataset_path, sample_size)
    
    model_id = "Qwen/Qwen3-4B"
    cache_dir = "/data/ruoyu/model"
    repeat_num = 1
    generate_python_file(the_dataset, model_id, cache_dir, repeat_num)