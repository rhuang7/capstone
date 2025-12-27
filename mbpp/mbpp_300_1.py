def check(candidate):
    assert candidate(1) == 2.0
    assert candidate(2) == 6.0
    assert candidate(3) == 20.0


def count_balanced_binary_sequences(n):
    from math import comb

    def count_with_sum(k):
        # Number of ways to get sum k in n bits
        return comb(n, k)

    total = 0
    for k in range(n + 1):
        total += count_with_sum(k) * count_with_sum(k)
    return total

check(count_balanced_binary_sequences)