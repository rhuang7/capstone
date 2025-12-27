def check(candidate):
    assert candidate((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert candidate((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert candidate((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)


def xor_tuples(tuples):
    if not tuples:
        return ()
    result = ()
    for i in range(len(tuples[0])):
        xor_value = 0
        for t in tuples:
            xor_value ^= t[i]
        result += (xor_value,)
    return result

check(xor_tuples)