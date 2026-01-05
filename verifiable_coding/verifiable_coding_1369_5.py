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

def compute_primes_sum(max_n):
    is_prime = sieve(max_n)
    prime_sum = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            prime_sum += i
    return prime_sum

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    test_cases = list(map(int, data[1:T+1]))
    max_n = max(test_cases)
    prime_sums = [0] * (max_n + 1)
    is_prime = sieve(max_n)
    prime_sum = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            prime_sum += i
        prime_sums[i] = prime_sum
    for n in test_cases:
        print(prime_sums[n])

if __name__ == '__main__':
    solve()