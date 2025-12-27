def check(candidate):
    assert candidate([1,2,3],[3,2,1],3,3) == True
    assert candidate([1,1,1],[2,2,2],3,3) == False
    assert candidate([8,9],[4,5,6],2,3) == False


def are_arrays_equal(arr1, arr2):
    return arr1 == arr2

check(are_arrays_equal)