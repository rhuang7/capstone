def check(candidate):
    assert candidate([12,33,23,10,67,89,45,667,23,12,11,10,54])==[3,11]
    assert candidate([1,2,2,2,4,4,4,5,5,5,5])==[0]
    assert candidate([2,1,5,6,8,3,4,9,10,11,8,12])==[1]


def find_min_indices(lst):
    if not lst:
        return []
    min_val = min(lst)
    return [i for i, x in enumerate(lst) if x == min_val]

check(find_min_indices)