def check(candidate):
    assert candidate([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19
    assert candidate([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 10
    assert candidate([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 1) == 11


def find_max_of_nth_column(tuples, n):
    if not tuples:
        return None
    if n < 0 or n >= len(tuples[0]):
        return None
    return max(t[ n ] for t in tuples)

check(find_max_of_nth_column)