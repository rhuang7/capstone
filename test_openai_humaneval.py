from datasets import load_from_disk
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
import random
import re
import time
import utils


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
    
    #store = random.sample(store, sample_size)
    return store

def do_test(testset, model_id, cache_dir, each_num):

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
    
    count_store = []
    total_len = len(testset)
    for i in tqdm(range(total_len), desc="processing"):
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
            
            base_code = current_case[2] + '\n\n' + raw_resp
            function_name = utils.extract_func_name(raw_resp)
            test_code = '\n\ncheck(' + function_name[-1] + ')'
            base_code += test_code
            
            python_file_name = current_case[0] + '.py'
            python_file_name = re.sub(r'/', '_', python_file_name)
            python_file_name = 'humaneval/' + python_file_name
            with open(python_file_name, 'w') as f:
                f.write(base_code)
            
        
    return count_store


if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/openai_humaneval"
    sample_size = 164
    
    the_dataset = fetch_data(dataset_path, sample_size)
    
    model_id = "Qwen/Qwen3-4B"
    cache_dir = "/data/ruoyu/model"
    repeat_num = 1
    
    rubb = do_test(the_dataset, model_id, cache_dir, repeat_num)
    
    