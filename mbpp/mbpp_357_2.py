def check(candidate):
    assert candidate([(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]) == 10
    assert candidate([(3, 5), (7, 8), (6, 2), (7, 11), (9, 8)]) == 11
    assert candidate([(4, 6), (8, 9), (7, 3), (8, 12), (10, 9)]) == 12


def find_max_in_tuples(tuples):
    if not tuples:
        return None
    max_value = max(t[0] for t in tuples)
    return max_value

check(find_max_in_tuples)