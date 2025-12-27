def check(candidate):
    assert candidate(13,9) == True
    assert candidate(15,8) == False
    assert candidate(2,4) == False


def differ_at_one_bit(a, b):
    xor = a ^ b
    return bin(xor).count('1') == 1

check(differ_at_one_bit)