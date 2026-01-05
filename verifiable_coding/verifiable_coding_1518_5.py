import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    # Precompute primes up to 1e5 using Sieve of Eratosthenes
    max_n = 100000
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(max_n)) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    # Precompute possible sums of K primes
    # We'll use dynamic programming to check if a number can be formed by sum of K primes
    # dp[i][j] = True if j can be formed by sum of i primes
    max_n = 100000
    max_k = 100000
    dp = [[False] * (max_n + 1) for _ in range(max_k + 1)]
    
    # Base case: sum of 1 prime is the prime itself
    for i in range(2, max_n + 1):
        if is_prime[i]:
            dp[1][i] = True
    
    # Fill the dp table
    for k in range(2, max_k + 1):
        for n in range(2, max_n + 1):
            for p in range(2, n):
                if is_prime[p] and dp[k-1][n-p]:
                    dp[k][n] = True
                    break
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        if K == 1:
            results.append('1' if is_prime[N] else '0')
        else:
            results.append('1' if dp[K][N] else '0')
    
    print('\n'.join(results))