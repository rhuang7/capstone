def check(candidate):
    assert candidate((10, 4, 5, 6), (5, 10)) == True
    assert candidate((1, 2, 3, 4), (5, 6)) == False
    assert candidate((7, 8, 9, 10), (10, 8)) == True


def is_subset(tuple1, tuple2):
    return tuple1 <= tuple2

check(is_subset)