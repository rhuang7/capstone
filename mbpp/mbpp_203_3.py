def check(candidate):
    assert candidate(4,8) == 2
    assert candidate(2,4) == 2
    assert candidate(1,2) == 2


def hamming_distance(a, b):
    return bin(a ^ b).count('1')

check(hamming_distance)