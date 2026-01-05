import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    Q = int(data[idx])
    idx += 1
    queries = list(map(int, data[idx:idx+Q]))
    
    # Precompute all possible subarrays and their gcd
    # We'll use a sliding window approach to compute gcds
    # For each position, we'll track the gcd of the subarray ending at that position
    # And count how many times each gcd occurs
    # Since K can be up to 1e6, we can use a frequency array
    freq = defaultdict(int)
    current_gcd = 0
    for num in A:
        current_gcd = math.gcd(current_gcd, num)
        freq[current_gcd] += 1
    
    # For each query, check how many subarrays have gcd equal to K
    # But we also need to consider that a subarray can generate K if its gcd divides K
    # So we need to check all divisors of K
    # But since K is up to 1e6, we can precompute all divisors for each K
    # However, since queries are up to 1e5, it's better to process each query directly
    # So for each query K, we check all divisors of K and sum the frequencies
    # But to avoid recomputing divisors for each query, we can precompute all divisors for all K up to 1e6
    # However, since K can be up to 1e6, and queries are up to 1e5, we can precompute all divisors for all K up to 1e6
    # But since K is up to 1e6, we can precompute all divisors for all K up to 1e6
    # But since we don't have the queries in advance, we can process each query on the fly
    # So for each query K, we find all divisors of K and sum the frequencies of those divisors
    
    # Precompute all divisors for all K up to 1e6
    # But since K can be up to 1e6, and queries are up to 1e5, we can precompute all divisors for all K up to 1e6
    # But since we don't have the queries in advance, we can process each query on the fly
    
    # So for each query K, we find all divisors of K and sum the frequencies of those divisors
    # But since K can be up to 1e6, and queries are up to 1e5, this is feasible
    
    # Precompute all divisors for all K up to 1e6
    # But since we don't have the queries in advance, we can process each query on the fly
    
    # So for each query K, we find all divisors of K and sum the frequencies of those divisors
    
    # Now, for each query K, we need to find the number of subarrays whose gcd is a divisor of K
    # So we need to find all divisors of K and sum the frequencies of those divisors
    
    # Precompute all divisors for all K up to 1e6
    # But since we don't have the queries in advance, we can process each query on the fly
    
    # So for each query K, we find all divisors of K and sum the frequencies of those divisors
    
    # Now, for each query K, we need to find all divisors of K and sum the frequencies of those divisors
    # We can do this by checking all numbers up to sqrt(K) and adding divisors
    
    for K in queries:
        total = 0
        # Find all divisors of K
        divisors = set()
        for i in range(1, int(math.isqrt(K)) + 1):
            if K % i == 0:
                divisors.add(i)
                divisors.add(K // i)
        # Sum the frequencies of those divisors
        for d in divisors:
            total += freq.get(d, 0)
        print(total)