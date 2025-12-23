import random
from tqdm import tqdm
import json
import ast

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
            sub_dict[data[2]] = [0, 0, []]
        if data[0] == data[1]:
            sub_dict[data[2]][0] += 1
            sub_dict[data[2]][1] += 1
        else:
            sub_dict[data[2]][0] += 1
        sub_dict[data[2]][2].append(data[3])
    
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
            sub_dict[data[1]] = [0, 0, []]
        if data[0] == data[1]:
            sub_dict[data[1]][0] += 1
            sub_dict[data[1]][1] += 1
        else:
            sub_dict[data[1]][0] += 1
        sub_dict[data[1]][2].append(data[3])
    
    out_file_name = 'output/' + out_file_name
    with open(out_file_name, 'w') as file:
        json.dump(json_data, file)
        
    return

def extract_func_name(code: str) -> str | None:
    tree = ast.parse(code)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            return node.name
    return None

def extract_all_func_names(code: str):
    tree = ast.parse(code)
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def rename_function_and_references(code: str, old_name: str, new_name: str) -> str:
    tree = ast.parse(code)

    class Renamer(ast.NodeTransformer):
        def visit_FunctionDef(self, node: ast.FunctionDef):
            if node.name == old_name:
                node.name = new_name
            self.generic_visit(node)
            return node

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
            if node.name == old_name:
                node.name = new_name
            self.generic_visit(node)
            return node

        def visit_Name(self, node: ast.Name):
            if node.id == old_name:
                node.id = new_name
            return node

        def visit_Attribute(self, node: ast.Attribute):
            self.generic_visit(node)
            return node

    new_tree = Renamer().visit(tree)
    ast.fix_missing_locations(new_tree)
    return ast.unparse(new_tree) + "\n"