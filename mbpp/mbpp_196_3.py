def check(candidate):
    assert candidate([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] , 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]
    assert candidate([(4, 5), (4,5), (6, 7), (1, 2, 3), (3, 4, 6, 7)] ,2) == [(1, 2, 3), (3, 4, 6, 7)]
    assert candidate([(1, 4, 4), (4, 3), (8, 6, 7), (1, ), (3, 6, 7)] , 3) == [(4, 3), (1,)]


def remove_tuples_with_length_k(tuples_list, k):
    return [t for t in tuples_list if len(t) != k]

check(remove_tuples_with_length_k)