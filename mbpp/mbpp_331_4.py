def check(candidate):
    assert candidate(2) == 1
    assert candidate(4) == 2
    assert candidate(6) == 1


def count_unset_bits(n):
    count = 0
    for i in range(32):  # Assuming 32-bit integer
        if not (n & (1 << i)):
            count += 1
    return count

check(count_unset_bits)