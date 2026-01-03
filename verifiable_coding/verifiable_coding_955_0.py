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
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes

primes = generate_primes_up_to(10000)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    index = 1
    for _ in range(T):
        N = int(data[index])
        index += 1
        count = 0
        for q in primes:
            if 2 * q >= N:
                break
            p = N - 2 * q
            if is_prime(p):
                count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()