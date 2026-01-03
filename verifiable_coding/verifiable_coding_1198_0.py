import sys
import math
from collections import defaultdict

def solve():
    import sys
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
    
    # Preprocess all possible subarrays
    # For each subarray, compute the GCD of its elements
    # A subarray can generate K if and only if K is a multiple of the GCD of the subarray
    # So for each possible GCD value, count the number of subarrays with that GCD
    
    # We'll use a dictionary to store the count of subarrays for each GCD
    gcd_counts = defaultdict(int)
    
    # For each starting index i
    for i in range(N):
        current_gcd = A[i]
        gcd_counts[current_gcd] += 1
        for j in range(i + 1, N):
            current_gcd = math.gcd(current_gcd, A[j])
            gcd_counts[current_gcd] += 1
    
    # Now process the queries
    for K in queries:
        # For each query K, count the number of subarrays whose GCD divides K
        # But since K can be up to 1e6, we need to check all possible GCDs that divide K
        # However, since K can be up to 1e6, we can precompute all possible divisors of K
        # and sum the counts of subarrays with GCD equal to each divisor
        # But since K can be up to 1e6 and Q is up to 1e5, we need an efficient way
        # So we'll precompute for all possible K up to 1e6, the count of subarrays whose GCD divides K
        # But since K can be up to 1e6, and there are 1e5 queries, it's better to process each query directly
        
        # For each query K, we need to find all GCDs that divide K and sum their counts
        # So for each query K, we iterate through all divisors of K and sum the counts
        # To find all divisors of K, we can do it in O(sqrt(K)) time
        
        # But since K can be up to 1e6, and Q is up to 1e5, this is feasible
        # So for each query K, we find all divisors of K and sum the counts of subarrays with GCD equal to each divisor
        
        # However, for K=0, the answer is 0 (since all subarrays have GCD >=1)
        # But according to the problem statement, K is at least 1
        
        # So we can proceed
        
        total = 0
        # Find all divisors of K
        divisors = set()
        for i in range(1, int(math.isqrt(K)) + 1):
            if K % i == 0:
                divisors.add(i)
                divisors.add(K // i)
        # Sum the counts of subarrays with GCD equal to each divisor
        for d in divisors:
            total += gcd_counts.get(d, 0)
        print(total)

if __name__ == '__main__':
    solve()