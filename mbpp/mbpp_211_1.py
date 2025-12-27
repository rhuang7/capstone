def check(candidate):
    assert candidate(2) == 1
    assert candidate(3) == 2
    assert candidate(1) == 1


def count_numbers_with_bits_set(oth, nth):
    count = 0
    for num in range(0, 2**32):
        if (num & (1 << oth)) and (num & (1 << nth)):
            count += 1
    return count

check(count_numbers_with_bits_set)