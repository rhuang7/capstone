def check(candidate):
    assert candidate((7, 8, 4, 5, 9, 10),(1, 5, 6) ) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
    assert candidate((8, 9, 5, 6, 10, 11),(2, 6, 7) ) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]
    assert candidate((9, 10, 6, 7, 11, 12),(3, 7, 8) ) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]


def zip_tuples(tuple1, tuple2):
    return list(zip(tuple1, tuple2))

check(zip_tuples)