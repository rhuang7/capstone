def check(candidate):
    assert candidate(10,2,13)==6
    assert candidate(15,12,43)==25
    assert candidate(17,9,18)==10


def ncr_mod(n, r, p):
    # Handle base cases
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1 % p
    
    # Initialize result
    result = 1
    
    # Compute nCr using multiplicative formula
    for i in range(r):
        result = (result * (n - i)) % p
        result = (result * pow(i + 1, p - 2, p)) % p
    
    return result

check(ncr_mod)