def check(candidate):
    assert candidate([1,4,3,5],[1,2],4,2) == False
    assert candidate([1,2,1],[1,2,1],3,3) == True
    assert candidate([1,0,2,2],[2,2,0],4,3) ==False


def is_subarray(main_array, sub_array):
    if not sub_array:
        return True
    for i in range(len(main_array) - len(sub_array) + 1):
        if main_array[i:i+len(sub_array)] == sub_array:
            return True
    return False

check(is_subarray)