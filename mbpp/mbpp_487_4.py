def check(candidate):
    assert candidate([(1, 3), (3, 2), (2, 1)] ) == [(2, 1), (3, 2), (1, 3)]
    assert candidate([(2, 4), (3, 3), (1, 1)] ) == [(1, 1), (3, 3), (2, 4)]
    assert candidate([(3, 9), (6, 7), (4, 3)] ) == [(4, 3), (6, 7), (3, 9)]


def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

check(sort_by_last_element)