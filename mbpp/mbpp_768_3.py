def check(candidate):
    assert candidate(13) == True
    assert candidate(21) == True
    assert candidate(18) == False


def has_odd_parity(n):
    return bin(n).count('1') % 2 == 1

check(has_odd_parity)