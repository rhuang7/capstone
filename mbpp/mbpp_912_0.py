def check(candidate):
    assert candidate(lobb_num(5, 3)) == 35
    assert candidate(lobb_num(3, 2)) == 5
    assert candidate(lobb_num(4, 2)) == 20


def lobb_number(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return lobb_number(n - 1) + lobb_number(n - 2)

check(lobb_number)