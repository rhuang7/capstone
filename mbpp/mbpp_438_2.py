def check(candidate):
    assert candidate([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '3'
    assert candidate([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '2'
    assert candidate([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == '4'


def count_bidirectional_pairs(pairs):
    """
    Count the number of bidirectional tuple pairs in a list of tuples.
    A bidirectional pair is defined as two tuples (a, b) and (b, a) that are present in the list.
    """
    seen = set()
    count = 0
    for a, b in pairs:
        if (b, a) in seen:
            count += 1
        seen.add((a, b))
    return count

check(count_bidirectional_pairs)