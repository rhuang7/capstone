def check(candidate):
    assert candidate(10, 2, 13) == 6
    assert candidate(11, 3, 14) == 11
    assert candidate(18, 14, 19) == 1


def ncr_mod(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1 % p
    # Compute factorial mod p
    def fact_mod(x, mod):
        res = 1
        for i in range(2, x + 1):
            res = (res * i) % mod
        return res
    # Compute ncr mod p using modular inverses
    numerator = (fact_mod(n, p) * fact_mod(n - r, p)) % p
    denominator = fact_mod(r, p)
    # Compute modular inverse of denominator using Fermat's little theorem
    inv_denominator = pow(denominator, p - 2, p)
    return (numerator * inv_denominator) % p

check(ncr_mod)