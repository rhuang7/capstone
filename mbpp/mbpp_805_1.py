def check(candidate):
    assert candidate([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12] 
    assert candidate([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10] 
    assert candidate([[2,3,1]])==[2,3,1] 


def find_highest_sum_list(list_of_lists):
    if not list_of_lists:
        return []
    
    max_sum = -float('inf')
    max_list = []
    
    for lst in list_of_lists:
        current_sum = sum(lst)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst
    
    return max_list

check(find_highest_sum_list)