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
import count_assert


def fetch_data(dataset_path, sample_size=164):
    ds = load_from_disk(dataset_path)
    
    id_list = ds["test"]["task_id"]
    prompt_list = ds["test"]["prompt"]
    test_list = ds["test"]["test"]
    
    store = []
    total_num = len(id_list)
    for i in tqdm(range(total_num), desc="Reading the dataset"):
        temp_list = [id_list[i], prompt_list[i], test_list[i]]
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
            python_file_name = 'humaneval/' + python_file_name
            with open(python_file_name, 'w') as f:
                f.write(base_code)
            after_num += 1
            
    return

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
        proc = subprocess.run(
            [python_exe, "count_actual_run.py", str(f)],
            capture_output=True,
            text=True,
        )
        
        path_name_list = str(f).split('/')
        key_name = path_name_list[1]

        passed = (proc.returncode == 0)
        results.append((f, passed, proc.returncode, proc.stdout, proc.stderr))
        if passed == 1:
            test_out = results[-1][3].splitlines()
            pass_info = test_out[1].split(' ')
            base_num_assert = count_assert.estimate_assert_runs(f)
        
            if key_name not in count_dict.keys():
                count_dict[key_name] = []
            count_dict[key_name].append(int(pass_info[1]))
            count_dict[key_name].append(base_num_assert)
        else:
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
    dataset_path = "/data/ruoyu/dataset/openai_humaneval"
    sample_size = 164
    the_dataset = fetch_data(dataset_path, sample_size)
    
    model_id = "Qwen/Qwen3-4B"
    cache_dir = "/data/ruoyu/model"
    repeat_num = 10
    generate_python_file(the_dataset, model_id, cache_dir, repeat_num)
    
    test_outcome_dict = run_many_py("./humaneval", "*.py")
    utils.creat_json_for_humaneval(test_outcome_dict, 'humaneval_out')
    
    