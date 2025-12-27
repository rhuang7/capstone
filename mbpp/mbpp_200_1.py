def check(candidate):
    assert candidate([12,33,23,10,67,89,45,667,23,12,11,10,54])==[7]
    assert candidate([1,2,2,2,4,4,4,5,5,5,5])==[7,8,9,10]
    assert candidate([2,1,5,6,8,3,4,9,10,11,8,12])==[11]


def find_max_indices(lst):
    if not lst:
        return []
    max_val = max(lst)
    return [i for i, x in enumerate(lst) if x == max_val]

check(find_max_indices)