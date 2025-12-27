def check(candidate):
    assert candidate([1,2,3,4,5], [5,6,7,8,9])==True
    assert candidate([1,2,3,4,5], [6,7,8,9])==None
    assert candidate(['a','b','c'], ['d','b','e'])==True


def has_common_element(list1, list2):
    return bool(set(list1) & set(list2))

check(has_common_element)