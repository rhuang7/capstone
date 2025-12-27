def check(candidate):
    assert candidate(36,57) == False
    assert candidate(2,4) == False
    assert candidate(23,47) == True


def are_divisor_sums_equal(a, b):
    def sum_of_divisors(n):
        if n == 0:
            return 0
        total = 1  # 1 is a divisor of all numbers
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total

    return sum_of_divisors(a) == sum_of_divisors(b)

check(are_divisor_sums_equal)