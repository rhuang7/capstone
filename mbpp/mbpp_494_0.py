def check(candidate):
    assert candidate((1, 1, 0, 1, 0, 0, 1)) == '105'
    assert candidate((0, 1, 1, 0, 0, 1, 0, 1)) == '101'
    assert candidate((1, 1, 0, 1, 0, 1)) == '53'


def binary_tuple_to_integer(binary_tuple):
    return int(''.join(map(str, binary_tuple)), 2)

check(binary_tuple_to_integer)