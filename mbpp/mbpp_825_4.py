def check(candidate):
    assert candidate([2,3,8,4,7,9],[0,3,5]) == [2, 4, 9]
    assert candidate([1, 2, 3, 4, 5],[1,2]) == [2,3]
    assert candidate([1,0,2,3],[0,1]) == [1,0]


def access_elements_by_index(lst, indices):
    return [lst[i] for i in indices]

check(access_elements_by_index)