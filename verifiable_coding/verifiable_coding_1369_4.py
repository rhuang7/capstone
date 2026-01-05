import sys
import math

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

def compute_primes_sum(n):
    if n < 2:
        return 0
    is_prime = sieve(n)
    total = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            total += i
    return total

def solve():
    import sys
    input = sys.stdin.buffer.read()
    data = input.split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    results = []
    max_n = max(cases)
    is_prime = sieve(max_n)
    prime_sums = [0] * (max_n + 1)
    current_sum = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            current_sum += i
        prime_sums[i] = current_sum
    for n in cases:
        results.append(str(prime_sums[n]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()