import json
import ECE_RMSCE
from tqdm import tqdm

def fetch_outcome(filename):
    path = './output/' + filename
    
    with open(path, "r") as f:
        data = json.load(f)

    return data

def calculate_ECE(data):
    acc_l = []
    conf_l = []
    
    for key in data.keys():
        content = data[key]
        acc_l.append(content[0])
        conf_l.append(content[1])
    
    base = 0
    for i in tqdm(range(len(acc_l)), desc="Calculate ECE"):
        ece = ECE_RMSCE.ece_from_bin_pairs(acc_l[i], conf_l[i])
        base += ece
    
    return base/len(acc_l)

def calculate_RMSCE(data):
    acc_l = []
    conf_l = []
    
    for key in data.keys():
        content = data[key]
        acc_l.append(content[0])
        conf_l.append(content[1])
    
    base = 0
    for i in tqdm(range(len(acc_l)), desc="Calculate RMSCE"):
        rmsce = ECE_RMSCE.rmsce_from_bin_pairs(acc_l[i], conf_l[i])
        base += rmsce
    
    return base/len(acc_l)

def convert_dict(current_data):
    out_dict = {}
    for key in current_data.keys():
        temp_dict = current_data[key]
        for t_key in temp_dict.keys():
            out_dict[t_key] = temp_dict[t_key]
    
    return out_dict

def sum_cal(file_list):
    for file in file_list:
        curr_data = fetch_outcome(file)
        type_check = list(curr_data.keys())
        if type(curr_data[type_check[0]]) != type([]):
            curr_data = convert_dict(curr_data)
        ece = calculate_ECE(curr_data)
        rmsce = calculate_RMSCE(curr_data)
        print('for file \'' + file + '\'')
        print('ECE is ' + str(ece))
        print('RMSCE is ' + str(rmsce))
        
    return

if __name__ == '__main__':
    files = ['humaneval_out', 'mbpp_out', 'verifiable_out', 'phase_one', 'multi_cate_out']
    sum_cal(files)
    