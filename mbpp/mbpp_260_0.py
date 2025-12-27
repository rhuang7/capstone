def check(candidate):
    assert candidate(3) == 7 
    assert candidate(4) == 17
    assert candidate(5) == 41


def newman_shanks_williams_prime(n):
    from sympy import isprime
    
    def newman_shanks_williams_number(k):
        return (2 ** (2 ** k)) + 1
    
    count = 0
    k = 0
    while True:
        num = newman_shanks_williams_number(k)
        if isprime(num):
            count += 1
            if count == n:
                return num
        k += 1

check(newman_shanks_williams_prime)