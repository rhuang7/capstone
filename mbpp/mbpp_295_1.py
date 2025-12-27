def check(candidate):
    assert candidate(8)==7
    assert candidate(12)==16
    assert candidate(7)==1


def sum_of_divisors(n):
    if n < 1:
        return 0
    total = 1  # 1 is a divisor of all positive integers
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

check(sum_of_divisors)