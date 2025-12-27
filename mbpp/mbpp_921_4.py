def check(candidate):
    assert candidate((10, 4, 5, 6, 7, 6, 8, 3, 4), 3) == [(10, 4, 5), (6, 7, 6), (8, 3, 4)]
    assert candidate((1, 2, 3, 4, 5, 6, 7, 8, 9), 2) == [(1, 2), (3, 4), (5, 6), (7, 8), (9,)]
    assert candidate((11, 14, 16, 17, 19, 21, 22, 25), 4) == [(11, 14, 16, 17), (19, 21, 22, 25)]


def chunk_tuples(tuples_list, n):
    """
    Splits a list of tuples into chunks of size n.
    """
    result = []
    for i in range(0, len(tuples_list), n):
        chunk = tuples_list[i:i+n]
        result.append(chunk)
    return result

check(chunk_tuples)