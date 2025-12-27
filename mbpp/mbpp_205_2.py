def check(candidate):
    assert candidate((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)
    assert candidate((2, 4, 5, 6, 1, 7)) == (-3, -5, -6, -7, -2, -8)
    assert candidate((8, 9, 11, 14, 12, 13)) == (-9, -10, -12, -15, -13, -14)


def count_inversions(tuples):
    inversions = 0
    n = len(tuples)
    for i in range(n):
        for j in range(i + 1, n):
            if tuples[i] > tuples[j]:
                inversions += 1
    return inversions

check(count_inversions)