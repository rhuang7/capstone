def check(candidate):
    assert candidate((1,2,3))==123
    assert candidate((4,5,6))==456
    assert candidate((5,6,7))==567


def tuple_to_integer(t):
    return int(''.join(map(str, t)))

check(tuple_to_integer)