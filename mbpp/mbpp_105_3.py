def check(candidate):
    assert candidate([True,False,True]) == 2
    assert candidate([False,False]) == 0
    assert candidate([True,True,True]) == 3


def count_true_booleans(lst):
    return sum(1 for item in lst if item)

check(count_true_booleans)