def check(candidate):
    assert candidate(2) == 1
    assert candidate(5) == 4
    assert candidate(14) == 17


def count_unset_bits(n):
    total = 0
    for i in range(1, n + 1):
        total += bin(i).count('0') - 1  # Subtract 1 to exclude the leading '0b' part
    return total

check(count_unset_bits)