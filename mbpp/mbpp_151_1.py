def check(candidate):
    assert candidate(17,13) == True
    assert candidate(15,21) == False
    assert candidate(25,45) == False


def is_coprime(a, b):
    from math import gcd
    return gcd(a, b) == 1

check(is_coprime)