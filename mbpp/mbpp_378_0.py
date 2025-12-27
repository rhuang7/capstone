def check(candidate):
    assert candidate([1,2,3,4]) == [4,1,2,3]
    assert candidate([0,1,2,3]) == [3,0,1,2]
    assert candidate([9,8,7,1]) == [1,9,8,7]


def shift_last_to_first(lst):
    if not lst:
        return lst
    return [lst[-1]] + lst[:-1]

check(shift_last_to_first)