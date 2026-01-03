import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    mod = M
    
    # Precompute factorial and inverse factorial modulo M
    max_n = N
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    # Precompute inverse factorial modulo M
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    # Function to compute binomial coefficient C(n, k) mod M
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod
    
    # Total number of strings of length N is 2^N
    total = pow(2, N, mod)
    
    # Subtract the number of periodic strings
    # A string is periodic if it can be written as v^n for some n >= 2
    # So we need to find the number of strings that are periodic and subtract them from total
    
    # Use inclusion-exclusion principle
    # For each divisor d of N where d < N, count the number of strings of length d that can be repeated to form a string of length N
    
    # We need to find for each d that divides N and d < N, the number of strings of length d that are not periodic
    # But since we are counting periodic strings, we need to find the number of strings of length d that can be repeated to form a string of length N
    
    # So for each divisor d of N where d < N, the number of periodic strings of length N that are formed by repeating a string of length d is 2^d - (number of non-periodic strings of length d)
    # But since we are counting periodic strings, we need to find the number of strings of length d that can be repeated to form a string of length N
    
    # However, for a string of length N to be periodic, it must be of the form v^n where v is a string of length d, and d divides N
    # So for each divisor d of N where d < N, the number of periodic strings of length N that are formed by repeating a string of length d is 2^d - (number of non-periodic strings of length d)
    
    # So the total number of periodic strings is sum over all d | N, d < N of (2^d - (number of non-periodic strings of length d))
    
    # But since we are trying to find the number of non-periodic strings, we need to subtract the periodic strings from the total
    
    # So the answer is total - sum over all d | N, d < N of (2^d - (number of non-periodic strings of length d))
    
    # To compute this, we need to find all divisors of N that are less than N
    
    # Find all divisors of N
    def get_divisors(n):
        divisors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i < n:
                    divisors.add(i)
                if n // i < n:
                    divisors.add(n // i)
        return sorted(divisors)
    
    divisors = get_divisors(N)
    
    # We need to compute the number of non-periodic strings of length d for each d in divisors
    # This is the same as the answer for N = d, which is 2^d - sum over all divisors of d that are less than d of (2^k - (number of non-periodic strings of length k))
    
    # We can memoize the results for each d
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def count_non_periodic(n):
        if n == 1:
            return 2  # Only 0 and 1, both are non-periodic
        total = pow(2, n, mod)
        divisors = get_divisors(n)
        for d in divisors:
            if d < n:
                total = (total - (pow(2, d, mod) - count_non_periodic(d))) % mod
        return total
    
    result = (total - sum((pow(2, d, mod) - count_non_periodic(d)) for d in divisors)) % mod
    print(result)

if __name__ == '__main__':
    solve()