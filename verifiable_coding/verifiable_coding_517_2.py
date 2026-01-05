import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    # Total number of strings of length N is 2^N
    total = pow(2, N, M)
    
    # We need to subtract the number of periodic strings
    # A string is periodic if it can be written as v^n for some n >= 2
    # So, we need to find the number of strings that are periodic and subtract them
    
    # We use inclusion-exclusion principle
    # For each divisor d of N where d < N, we count the number of strings that are periodic with period d
    # But we have to be careful not to double count
    
    # We precompute the divisors of N
    def get_divisors(n):
        divisors = set()
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                if n // i != i:
                    divisors.add(n // i)
        divisors.add(n)
        return sorted(divisors)
    
    divisors = get_divisors(N)
    
    # We use Möbius function for inclusion-exclusion
    # Precompute Möbius function for numbers up to N
    def mobius(n):
        mu = [1] * (n + 1)
        is_prime = [True] * (n + 1)
        for i in range(2, n + 1):
            if is_prime[i]:
                for j in range(i, n + 1, i):
                    is_prime[j] = False
                    mu[j] *= -1
                for j in range(i, n + 1, i * i):
                    mu[j] = 0
        return mu
    
    mu = mobius(N)
    
    # Now, for each divisor d of N, we calculate the number of strings of length d that are periodic
    # The number of such strings is 2^d - 2^(d-1) = 2^(d-1)
    # But we have to multiply by the Möbius function to account for inclusion-exclusion
    # The formula is: sum_{d | N, d < N} mu(d) * 2^{N/d - 1}
    
    result = 0
    for d in divisors:
        if d == N:
            continue
        k = N // d
        term = mu[d] * pow(2, k - 1, M)
        result = (result + term) % M
    
    # The answer is total - result
    answer = (total - result) % M
    print(answer)

if __name__ == '__main__':
    solve()