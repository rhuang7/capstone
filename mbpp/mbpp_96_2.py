def check(candidate):
    assert candidate(15) == 4 
    assert candidate(12) == 6
    assert candidate(9) == 3


def count_divisors(n):
    if n == 0:
        return 0
    count = 0
    sqrt_n = int(n ** 0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

check(count_divisors)