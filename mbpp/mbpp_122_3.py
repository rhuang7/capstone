def check(candidate):
    assert candidate(1) == 30
    assert candidate(50) == 273
    assert candidate(1000) == 2664


def is_smart_number(n):
    # A smart number is a number that is a multiple of a perfect number
    # Perfect number is a number that is equal to the sum of its proper divisors
    def is_perfect(num):
        if num < 6:
            return False
        sum_divisors = 1  # 1 is a proper divisor for all numbers > 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i
        return sum_divisors == num

    # Check if n is a multiple of a perfect number
    for i in range(6, n + 1, 2):  # Start from 6, the first perfect number
        if n % i == 0:
            return True
    return False

def nth_smart_number(n):
    count = 0
    num = 1
    while count < n:
        if is_smart_number(num):
            count += 1
        num += 1
    return num - 1

check(nth_smart_number)