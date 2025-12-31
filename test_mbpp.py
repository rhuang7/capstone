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

def strip_code_fences(s: str) -> str:
    s = s.strip()
    # remove ```python ... ``` fences if present
    if s.startswith("```"):
        s = re.sub(r"^```[a-zA-Z0-9_+-]*\s*", "", s)
        s = re.sub(r"\s*```$", "", s)
    return s.strip()

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
    
    store = random.sample(store, sample_size)
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
                {"role":"user","content": """You are a Python coding assistant.

Write Python code that solves the following programming task.

Requirements:
- Output ONLY valid Python code. No markdown, no explanations.
- Implement the solution as one or more function definitions (no input()).
- Choose clear function name(s) and parameter names that match the task description.
- Ensure correctness for typical edge cases.
- You may import standard library modules if needed.

TASK:
""" + prompt}
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
            
            # temp_lines = current_case[1].splitlines()
            # import_line = '\n'
            # for line in temp_lines:
            #     if 'import' in line:
            #         import_line += line + '\n'
            # raw_resp = "\n".join('    ' + line for line in raw_resp.splitlines())
            
            # base_code = current_case[2] + '\n\n' + import_line + raw_resp
            base_code = current_case[2] + '\n\n' + raw_resp
            ast_work = 0
            try:
                test_func_name = utils.extract_func_name(raw_resp)
            except SyntaxError:
                ast_work = 1
                pass
            except IndentationError:
                ast_work = 1
                pass
            if ast_work == 1:
                re_mod = re.compile(r'^\s*(?:async\s+)?def\s+([A-Za-z_]\w*)\s*\(', re.M)
                code = strip_code_fences(raw_resp)
                m = re_mod.search(code)
                if m:
                    test_func_name = m.group(1)
                else:
                    test_func_name = None
            
            test_code = '\n\ncheck(' + test_func_name[-1] + ')'
            base_code += test_code
            
            python_file_name = 'mbpp_' + str(current_case[0]) + '_' + str(after_num) + '.py'
            python_file_name = re.sub(r'/', '_', python_file_name)
            conf_key = python_file_name
            python_file_name = 'mbpp/' + python_file_name
            with open(python_file_name, 'w') as f:
                f.write(base_code)
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
            conf_dict[conf_key] = the_conf
            
    return conf_dict

def run_many_py(folder: str | Path, pattern: str = "*.py", python_exe: str | None = None):
    folder = Path(folder)
    python_exe = python_exe or sys.executable

    files = sorted(folder.rglob(pattern), key=utils.human_eval_id)
    if not files:
        print(f"No files matched: {folder} / {pattern}")
        return 0

    ok, failed = 0, 0
    results = []
    count_dict = {}
    
    for i in tqdm(range(len(files)), desc="Testing Generated Code"):
        f = files[i]
        timedout = 0
        try:
            proc = subprocess.run(
                [python_exe, "count_actual_run.py", str(f)],
                capture_output=True,
                text=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired as e:
            proc = None
            timedout = 1
        
        path_name_list = str(f).split('/')
        key_name = path_name_list[1]

        if timedout == 0:
            passed = (proc.returncode == 0)
            results.append((f, passed, proc.returncode, proc.stdout, proc.stderr))
            if passed == 1:
                test_out = results[-1][3].splitlines()
                base_num_assert = count_assert.estimate_assert_runs(f)
                
                if key_name not in count_dict.keys():
                    count_dict[key_name] = []
                for info in test_out:
                    if 'Passed: ' in info:
                        info = info.split(' ')
                        count_dict[key_name].append(int(info[1]))
                count_dict[key_name].append(base_num_assert)
            else:
                if key_name not in count_dict.keys():
                    count_dict[key_name] = []
                count_dict[key_name].append(0)
                count_dict[key_name].append(-1)
        else:
            passed = 0
            if key_name not in count_dict.keys():
                count_dict[key_name] = []
            count_dict[key_name].append(0)
            count_dict[key_name].append(-1)
        
        if passed:
            ok += 1
        else:
            failed += 1
            
    print(f"Done. PASS={ok}, FAIL={failed}, TOTAL={len(files)}")

    return count_dict

if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/mbpp"
    sample_size = 974
    the_dataset = fetch_data(dataset_path, sample_size)
    
    model_id = "Qwen/Qwen3-4B"
    cache_dir = "/data/ruoyu/model"
    repeat_num = 5
    the_conf = generate_python_file(the_dataset, model_id, cache_dir, repeat_num)
    
    test_outcome_dict = run_many_py("./mbpp", "*.py")
    print(test_outcome_dict.keys())
    print(the_conf.keys())
    utils.creat_json_for_humaneval(test_outcome_dict, 'mbpp_out', the_conf)
    