def check(candidate):
    assert candidate(30) == 24
    assert candidate(18) == 13
    assert candidate(2) == 1


def sum_of_odd_factors(n):
    if n < 1:
        return 0
    sum_factors = 1
    i = 3
    while i * i <= n:
        if n % i == 0:
            is_odd = True
            while n % i == 0:
                n //= i
                if i % 2 == 0:
                    is_odd = False
            if is_odd:
                sum_factors *= i
        i += 2
    if n > 1:
        if n % 2 == 1:
            sum_factors *= n
    return sum_factors

check(sum_of_odd_factors)