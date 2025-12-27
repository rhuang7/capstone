def check(candidate):
    assert candidate([1,2,3,4]) == [2,3,4,1]
    assert candidate([2,3,4,1,5,0]) == [3,4,1,5,0,2]
    assert candidate([5,4,3,2,1]) == [4,3,2,1,5]


def shift_first_to_end(lst):
    if len(lst) == 0:
        return lst
    return lst[1:] + [lst[0]]

check(shift_first_to_end)