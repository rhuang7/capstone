def check(candidate):
    assert candidate((8, 2, 3, -1, 7))==-67.2
    assert candidate((-10,-20,-30))==-2000.0
    assert candidate((19,15,18))==1710.0


def multiply_and_divide(lst):
    if not lst:
        return 0
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)

check(multiply_and_divide)