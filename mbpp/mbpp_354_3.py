def check(candidate):
    assert candidate(1,5,2)==9
    assert candidate(2,6,4)==22
    assert candidate(1,4,5)==16


def find_nth_term(a, d, n):
    return a + (n - 1) * d

check(find_nth_term)