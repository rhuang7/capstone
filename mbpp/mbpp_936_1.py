def check(candidate):
    assert candidate([(4, 3), (1, 9), (2, 10), (3, 2)],  [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]
    assert candidate([(5, 4), (2, 10), (3, 11), (4, 3)],  [3, 4, 2, 3]) == [(3, 11), (4, 3), (2, 10), (3, 11)]
    assert candidate([(6, 3), (3, 8), (5, 7), (2, 4)],  [2, 5, 3, 6]) == [(2, 4), (5, 7), (3, 8), (6, 3)]


def rearrange_tuples(tuples_list, order):
    return [tuples_list[i] for i in order]

check(rearrange_tuples)