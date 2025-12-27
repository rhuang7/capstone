def check(candidate):
    assert candidate([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]
    assert candidate([(1, 2, 3), (4, 2, 3), (7, 8)]) == [1, 2, 3, 4, 7, 8]
    assert candidate([(7, 8, 9), (10, 11, 12), (10, 11)]) == [7, 8, 9, 10, 11, 12]


def extract_single_occurrences(tup):
    from collections import Counter
    count = Counter(tup)
    return [item for item in tup if count[item] == 1]

check(extract_single_occurrences)