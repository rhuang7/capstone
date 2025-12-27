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
    return store


if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/mbpp"
    sample_size = 974
    the_dataset = fetch_data(dataset_path, sample_size)
    
    print(the_dataset[0])