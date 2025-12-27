def check(candidate):
    assert candidate((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
    assert candidate((11, 5, 6, 7), (6, 7, 8, 6)) == (1771561, 78125, 1679616, 117649)
    assert candidate((12, 6, 7, 8), (7, 8, 9, 7)) == (35831808, 1679616, 40353607, 2097152)


def exponentiate_tuples(tuple1, tuple2):
    return tuple(x ** y for x, y in zip(tuple1, tuple2))

check(exponentiate_tuples)