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

def generate_primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    max_n = max(cases) if cases else 0
    primes = generate_primes_up_to(max_n + 2)
    
    prime_set = set(primes)
    
    results = []
    for N in cases:
        count = 0
        for q in primes:
            if 2 * q > N:
                break
            p = N - 2 * q
            if p in prime_set:
                count += 1
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()