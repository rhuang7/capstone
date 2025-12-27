def check(candidate):
    assert candidate([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert candidate([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert candidate([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1


def find_element_after_rotations(arr, rotations, index):
    n = len(arr)
    effective_rotations = rotations % n
    new_index = (index - effective_rotations) % n
    return arr[new_index]

check(find_element_after_rotations)