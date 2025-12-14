
def get_accuracy(result_list):
    total_sample_num = len(result_list)
    total_count = 0
    for i in result_list:
        if i[0] == i[1]:
            total_count += 1
    
    out = total_count/total_sample_num
    
    return out