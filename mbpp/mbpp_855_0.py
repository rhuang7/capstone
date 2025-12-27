def check(candidate):
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(18) == True


def has_even_parity(n):
    return (n & (n - 1)) == 0

check(has_even_parity)