def check(candidate):
    assert candidate([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
    assert candidate([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
    assert candidate([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4


def tuple_frequency(lst):
    from collections import defaultdict

    freq = defaultdict(int)
    for item in lst:
        freq[item] += 1
    return dict(freq)

check(tuple_frequency)