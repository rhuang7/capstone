def check(candidate):
    assert candidate(16) == 33
    assert candidate(2) == 2
    assert candidate(14) == 28


def count_total_set_bits(n):
    def count_set_bits(num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    total = 0
    for i in range(1, n + 1):
        total += count_set_bits(i)
    return total

check(count_total_set_bits)