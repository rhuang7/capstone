
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
    
    return out_dict

def print_accuracy_by_category(in_dict):
    cate_acc = get_accuracy_by_category(in_dict)
    for key in cate_acc.keys():
        print("For category -", key, "- the accuracy is ", cate_acc[key])
    
    return