import sys

import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    # Precompute primes up to 1e5 using Sieve of Eratosthenes
    max_n = 10**5
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    # Precompute possible sums of K primes
    # We'll use dynamic programming to check if a number can be formed by sum of K primes
    # dp[k][n] = True if n can be formed by sum of k primes
    # Since N can be up to 1e5 and K up to 1e5, we need to optimize
    # We'll use a 2D array where dp[k][n] is True if n can be formed by sum of k primes
    
    # Since K can be up to 1e5 and N up to 1e5, we need to optimize
    # We'll use a list of sets: for each k, store the set of numbers that can be formed by sum of k primes
    # Initialize for k=1: all primes
    max_k = 10**5
    max_n = 10**5
    dp = [set() for _ in range(max_k + 1)]
    for i in range(2, max_n + 1):
        if is_prime[i]:
            dp[1].add(i)
    
    # Fill dp for k >= 2
    for k in range(2, max_k + 1):
        for i in range(2, max_n + 1):
            for p in dp[k-1]:
                if p + i <= max_n:
                    dp[k].add(p + i)
    
    # Process test cases
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        if K == 1:
            results.append('1' if is_prime[N] else '0')
        else:
            results.append('1' if N in dp[K] else '0')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()