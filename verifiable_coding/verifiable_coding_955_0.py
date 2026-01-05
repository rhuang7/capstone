import sys
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.isqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def generate_primes_up_to(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    max_n = max(cases) if cases else 0
    max_possible_q = (max_n) // 2  # since 2q <= N => q <= N/2
    
    primes = generate_primes_up_to(max_possible_q)
    
    prime_set = set(primes)
    
    result = []
    for N in cases:
        count = 0
        for q in primes:
            if 2 * q > N:
                break
            p = N - 2 * q
            if p in prime_set:
                count += 1
        result.append(str(count))
    
    print('\n'.join(result))

if __name__ == '__main__':
    solve()