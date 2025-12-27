def check(candidate):
    assert candidate(24) == 3
    assert candidate(12) == 2
    assert candidate(4) == 1


def count_distinct_prime_powers(n):
    if n < 2:
        return 0
    
    distinct_powers = set()
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                n //= i
                power += 1
            distinct_powers.add(power)
        i += 1
    
    if n > 1:
        distinct_powers.add(1)  # remaining prime factor
    
    return len(distinct_powers)

check(count_distinct_prime_powers)