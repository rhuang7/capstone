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
    # For each position i, keep track of the gcd of subarrays ending at i
    # This is based on the fact that a subarray can generate K if and only if K is a multiple of the gcd of the subarray
    # So for each subarray, we compute its gcd and count how many times each gcd occurs
    # Then for each query K, we count how many subarrays have a gcd that divides K
    
    # We use a dictionary to count the frequency of each gcd
    gcd_count = defaultdict(int)
    current_gcd = 0
    
    for num in A:
        current_gcd = math.gcd(current_gcd, num)
        gcd_count[current_gcd] += 1
    
    # Now for each query K, we count the number of subarrays whose gcd divides K
    # To do this efficiently, we precompute all possible gcd values and their counts
    # Then for each query K, we iterate through all possible divisors of K and sum their counts
    
    # Precompute all divisors for each K up to 1e6
    # But since K can be up to 1e6, we can precompute the divisors on the fly for each query
    # However, for efficiency, we can precompute all possible divisors for all K up to 1e6
    
    # Precompute divisors for all K up to 1e6
    max_k = 10**6
    divisors = [[] for _ in range(max_k + 1)]
    for i in range(1, max_k + 1):
        for j in range(i, max_k + 1, i):
            divisors[j].append(i)
    
    # Now process queries
    for K in queries:
        total = 0
        for d in divisors[K]:
            total += gcd_count.get(d, 0)
        print(total)
        
if __name__ == '__main__':
    solve()