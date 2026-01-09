import random
from tqdm import tqdm
import json
import ast
from pathlib import Path
import re

def get_accuracy(result_list):
    total_sample_num = len(result_list)
    total_count = 0
    for i in result_list:
        if i[0] == i[1]:
            total_count += 1
    
    out = total_count/total_sample_num
    
    return out

def get_accuracy_by_category(result_list):
    out_dict = {}
    for i in result_list:
        if i[0] not in out_dict.keys():
            out_dict[i[0]] = [0, 0]
            
        if i[0] == i[1]:
            out_dict[i[0]][0] += 1
            out_dict[i[0]][1] += 1
        else:
            out_dict[i[0]][0] += 1
         
    acc_dict = {}   
    for key in out_dict.keys():
        acc_dict[key] = out_dict[key][1] / out_dict[key][0]
    
    return acc_dict

def print_accuracy_by_category(in_dict):
    cate_acc = get_accuracy_by_category(in_dict)
    for key in cate_acc.keys():
        print("For category -", key, "- the accuracy is ", cate_acc[key])
    
    return

def rand_nonneg_ints_sum(total, n):
    m = total + n - 1
    bars = sorted(random.sample(range(m), n - 1))
    nums = []
    prev = -1
    for b in bars + [m]:
        nums.append(b - prev - 1)
        prev = b
    return nums

def testset_convertage(testset):
    out_list = []
    labels = list(testset.keys())
    for t in tqdm(range(len(labels)), desc="Converting to List"):
        label = labels[t]
        for content in testset[label]:
            current_list = [label]
            current_list.extend(content)
            out_list.append(current_list)
    
    return out_list

def get_accuracy_by_category_multi(result_list):
    out_dict = {}
    for i in result_list:
        if i[2] not in out_dict.keys():
            out_dict[i[2]] = [0, 0]
            
        if i[0] == i[1]:
            out_dict[i[2]][0] += 1
            out_dict[i[2]][1] += 1
        else:
            out_dict[i[2]][0] += 1
         
    acc_dict = {}   
    for key in out_dict.keys():
        acc_dict[key] = out_dict[key][1] / out_dict[key][0]
    
    return acc_dict

def print_accuracy_by_category_multi(in_dict):
    cate_acc = get_accuracy_by_category_multi(in_dict)
    for key in cate_acc.keys():
        print("For category -", key, "- the accuracy is ", cate_acc[key])
    
    return

def creat_json_for_phase_one(data_list, out_file_name):
    json_data = {}
    for i in tqdm(range(len(data_list)), desc="Store results into file"):
        data = data_list[i]
        if data[1] not in json_data.keys():
            json_data[data[1]] = {}
        sub_dict = json_data[data[1]]
        if data[2] not in sub_dict.keys():
            sub_dict[data[2]] = [[], []]
        if data[0] == data[1]:
            sub_dict[data[2]][0].append(1)
        else:
            sub_dict[data[2]][0].append(0)
        sub_dict[data[2]][1].append(data[3])
    
    out_file_name = 'output/' + out_file_name
    with open(out_file_name, 'w') as file:
        json.dump(json_data, file)
        
    return
        
def creat_json_for_phase_third(data_list, out_file_name):
    json_data = {}
    for i in tqdm(range(len(data_list)), desc="Store results into file"):
        data = data_list[i]
        if data[2] not in json_data.keys():
            json_data[data[2]] = {}
        sub_dict = json_data[data[2]]
        if data[1] not in sub_dict.keys():
            sub_dict[data[1]] = [[], []]
        if data[0] == data[1]:
            sub_dict[data[1]][0].append(1)
        else:
            sub_dict[data[1]][0].append(0)
        sub_dict[data[1]][1].append(data[3])
    
    out_file_name = 'output/' + out_file_name
    with open(out_file_name, 'w') as file:
        json.dump(json_data, file)
        
    return

def creat_json_for_humaneval(data_dict, out_file_name, conf_dict):
    local_dict = {}
    keys = list(data_dict.keys())
    for i in tqdm(range(len(keys)), desc="Storing the data"):
        current_key = keys[i]
        current_data = data_dict[current_key]
        current_conf = conf_dict[current_key]
        
        current_key_list = current_key.split('_')
        store_key = current_key_list[0] + '_' + current_key_list[1]
        if store_key not in local_dict.keys():
            local_dict[store_key] = [[], []]
        
        if current_data[1] >= 0:
            mark = current_data[0] / current_data[1]
        else: 
            mark = 0
        local_dict[store_key][0].append(mark)
        local_dict[store_key][1].append(current_conf)
    
    out_file_name = 'output/' + out_file_name
    with open(out_file_name, 'w') as file:
        json.dump(local_dict, file)
        
    return

def extract_func_name(code: str):
    tree = ast.parse(code)
    out = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            out.append(node.name)
    return out

def human_eval_id(p):
    m = re.search(r'HumanEval_(\d+)\.py$', p.name)
    return int(m.group(1)) if m else float("inf")

def mbpp_id(p):
    m = re.search(r'mbpp_(\d+)\.py$', p.name)
    return int(m.group(1)) if m else float("inf")

def verifiable_coding_id(p):
    m = re.search(r'verifiable_coding_(\d+)\.py$', p.name)
    return int(m.group(1)) if m else float("inf")

def creat_json_for_eval(data_dict, out_file_name, conf_dict):
    local_dict = {}
    keys = list(data_dict.keys())
    for i in tqdm(range(len(keys)), desc="Storing the data"):
        current_key = keys[i]
        current_data = data_dict[current_key]
        current_conf = conf_dict[current_key]
        
        current_key_list = current_key.split('_')
        store_key = current_key_list[0] + '_' + current_key_list[1] + '_' + current_key_list[2]
        if store_key not in local_dict.keys():
            local_dict[store_key] = [[], []]
        
        if current_data[1] >= 0:
            mark = current_data[0] / current_data[1]
        else: 
            mark = 0
        local_dict[store_key][0].append(mark)
        local_dict[store_key][1].append(current_conf)
    
    out_file_name = 'output/' + out_file_name
    with open(out_file_name, 'w') as file:
        json.dump(local_dict, file)
        
    return

def key_name_update(the_name):
    the_name_list = the_name.split('_')
    out_name = ''
    for n in the_name_list:
        out_name = out_name + n
        if n.isdigit():
            out_name += '.py'
            break
        out_name += '_'
    
    return out_name