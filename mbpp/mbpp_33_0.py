def check(candidate):
    assert candidate(10) == 1010
    assert candidate(1) == 1
    assert candidate(20) == 10100


def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

check(decimal_to_binary)