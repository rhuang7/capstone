import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    # Precompute primes up to 1e5 using Sieve of Eratosthenes
    max_n = 10**5
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(max_n)) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    # Precompute possible sums of K primes
    # We'll use dynamic programming to check if a number can be formed as sum of K primes
    # dp[k][n] = True if n can be formed as sum of k primes
    # Since N can be up to 1e5 and K up to 1e5, we need a space-efficient approach
    # We'll use a 1D array for each K, but since K can be up to 1e5, we'll use a list of sets
    
    # Initialize a list of sets for each K
    # dp[k] is a set of numbers that can be formed as sum of k primes
    # We'll precompute up to max N (1e5)
    max_k = 10**5
    dp = [set() for _ in range(max_k + 1)]
    
    # Base case: sum of 1 prime
    for prime in range(2, max_n + 1):
        if is_prime[prime]:
            dp[1].add(prime)
    
    # Fill the dp table
    for k in range(2, max_k + 1):
        for prime in range(2, max_n + 1):
            if is_prime[prime]:
                for prev in dp[k-1]:
                    if prev + prime <= max_n:
                        dp[k].add(prev + prime)
    
    # Process each test case
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        if K == 1:
            # Only possible if N is prime
            results.append('1' if is_prime[N] else '0')
        else:
            # Check if N can be formed as sum of K primes
            results.append('1' if N in dp[K] else '0')
    
    print('\n'.join(results))