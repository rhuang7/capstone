def check(candidate):
    assert candidate([0,1,2,3,4,5],6,1) == 0
    assert candidate([1,2,1,3,4],5,2) == 1
    assert candidate([2,3,4,3,5,7,1,2,3,5],10,2) == 2


def find_first_element_occuring_k_times(arr, k):
    from collections import Counter
    
    count = Counter(arr)
    for num in arr:
        if count[num] == k:
            return num
    return None

check(find_first_element_occuring_k_times)