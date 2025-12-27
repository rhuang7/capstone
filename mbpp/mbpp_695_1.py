def check(candidate):
    assert candidate((10, 4, 5), (13, 5, 18)) == True
    assert candidate((1, 2, 3), (2, 1, 4)) == False
    assert candidate((4, 5, 6), (5, 6, 7)) == True


def check_tuple_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return False
    for i in range(len(tuple1)):
        if tuple2[i] <= i:
            return False
    return True

check(check_tuple_elements)