def check(candidate):
    assert candidate([1,2,3]) == [3,2,1]
    assert candidate([1,2,3,4,4]) == [4,2,3,4,1]
    assert candidate([4,5,6]) == [6,5,4]


def interchange_first_last(lst):
    if len(lst) == 0:
        return lst
    if len(lst) == 1:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

check(interchange_first_last)