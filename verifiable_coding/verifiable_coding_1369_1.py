import sys
import math

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def precompute_primes_sum(max_n):
    is_prime = sieve(max_n)
    prime_sum = [0] * (max_n + 1)
    current_sum = 0
    for i in range(max_n + 1):
        if is_prime[i]:
            current_sum += i
        prime_sum[i] = current_sum
    return prime_sum

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    test_cases = list(map(int, data[1:T+1]))
    max_n = max(test_cases) if test_cases else 0
    if max_n < 2:
        for _ in test_cases:
            print(0)
        return
    prime_sum = precompute_primes_sum(max_n)
    for n in test_cases:
        print(prime_sum[n])

if __name__ == '__main__':
    solve()