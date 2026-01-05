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

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    primes = []
    i = 1
    while len(primes) < 10000:
        if is_prime(i):
            primes.append(i)
        i += 1
    for j in range(1, T + 1):
        N = int(data[j])
        count = 0
        for q in primes:
            if 2 * q > N:
                break
            p = N - 2 * q
            if p > 0 and is_prime(p):
                count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()