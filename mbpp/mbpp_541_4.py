def check(candidate):
    assert candidate(12) == True
    assert candidate(15) == False
    assert candidate(18) == True


def is_abundant(n):
    if n < 1:
        return False
    sum_of_divisors = 1  # 1 is a divisor of all positive integers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i
    return sum_of_divisors > n

check(is_abundant)