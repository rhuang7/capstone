def check(candidate):
    assert candidate([1,2,3]) == True
    assert candidate([1,2,1,2]) == False
    assert candidate([1,2,3,4,5]) == True


def are_elements_unique(lst):
    return len(lst) == len(set(lst))

check(are_elements_unique)