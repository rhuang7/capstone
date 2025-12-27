def check(candidate):
    assert candidate(10) == 17
    assert candidate(20) == 77
    assert candidate(5) == 10


def sum_of_primes(n):
    if n < 2:
        return 0
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return sum(num for num in range(2, n + 1) if is_prime(num))

check(sum_of_primes)