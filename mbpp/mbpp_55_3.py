def check(candidate):
    assert candidate(1,5,2)==16
    assert candidate(1,5,4)==256
    assert candidate(2,6,3)==486


def geometric_series_term(n, a, r):
    return a * (r ** n)

check(geometric_series_term)