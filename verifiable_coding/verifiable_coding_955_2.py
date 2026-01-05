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

def precompute_primes_up_to_max_n(max_n):
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.isqrt(max_n)) + 1):
        if primes[i]:
            for j in range(i*i, max_n + 1, i):
                primes[j] = False
    return [i for i, is_p in enumerate(primes) if is_p]

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    N_list = list(map(int, input[1:T+1]))
    
    max_N = max(N_list) if N_list else 0
    max_prime_needed = max_N + 2 * 2  # 2q can be up to 2*2=4, so p can be up to N - 4
    
    primes = precompute_primes_up_to_max_n(max_prime_needed)
    prime_set = set(primes)
    
    results = []
    for N in N_list:
        count = 0
        for q in primes:
            if 2 * q > N:
                break
            p = N - 2 * q
            if p in prime_set:
                count += 1
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()