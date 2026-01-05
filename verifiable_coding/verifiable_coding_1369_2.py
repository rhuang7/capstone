import sys
import math

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def sum_primes_up_to(n):
    if n < 2:
        return 0
    is_prime = sieve(n)
    return sum(i for i in range(2, n + 1) if is_prime[i])

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    results = []
    max_n = max(cases) if cases else 0
    is_prime = sieve(max_n)
    prefix_sum = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (i if is_prime[i] else 0)
    for n in cases:
        results.append(str(prefix_sum[n]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()