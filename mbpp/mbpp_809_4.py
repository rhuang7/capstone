def check(candidate):
    assert candidate((1, 2, 3), (2, 3, 4)) == False
    assert candidate((4, 5, 6), (3, 4, 5)) == True
    assert candidate((11, 12, 13), (10, 11, 12)) == True


def check_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return False
    for i in range(len(tuple1)):
        if tuple2[i] >= tuple1[i]:
            return False
    return True

check(check_elements)