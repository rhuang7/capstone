def check(candidate):
    assert candidate([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]
    assert candidate([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]
    assert candidate([0,0,0,0,0],5)==[0]


def extract_continuous_elements(lst, num_elements):
    if not lst or num_elements <= 0:
        return []
    if num_elements > len(lst):
        return lst
    return lst[:num_elements]

check(extract_continuous_elements)