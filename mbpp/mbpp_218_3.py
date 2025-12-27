def check(candidate):
    assert candidate(2,4) == 1
    assert candidate(4,10) == 4
    assert candidate(1,4) == 3


def min_operations_to_equal(a, b):
    operations = 0
    while a != b:
        if a > b:
            a = a // 2
            operations += 1
        else:
            b = b // 2
            operations += 1
    return operations

check(min_operations_to_equal)