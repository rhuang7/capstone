def check(candidate):
    assert candidate([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]
    assert candidate([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']
    assert candidate([[1, 2, 3], [4, 5]]) == [3, 5]


def get_last_elements(list_of_lists):
    return [sublist[-1] for sublist in list_of_lists]

check(get_last_elements)