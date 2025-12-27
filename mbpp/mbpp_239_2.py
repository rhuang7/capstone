def check(candidate):
    assert candidate(10, 4) == 4
    assert candidate(5, 2) == 6
    assert candidate(16, 3) == 84


def count_sequences(n, m):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(pos, last):
        if pos == n:
            return 1
        total = 0
        start = last + 1
        end = min(m, last * 2)
        for next_val in range(start, end + 1):
            total += dp(pos + 1, next_val)
        return total

    return dp(0, 0)

check(count_sequences)