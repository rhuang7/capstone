def check(candidate):
    assert candidate(8) == '1000'
    assert candidate(18) == '10010'
    assert candidate(7) == '111' 


def decimal_to_binary(n):
    if n < 0:
        return "Negative numbers cannot be converted to binary in this context."
    return bin(n)[2:]

check(decimal_to_binary)