def check(candidate):
    assert candidate([1,2,4,6,8,10,12,14,16,17])==True
    assert candidate([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert candidate([1, 2, 4, 6, 8, 10,15,14,20])==False


def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

check(is_sorted)