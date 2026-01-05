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
    
    # Precompute all possible subarrays and their gcds
    # For each subarray, the gcd of its elements is the smallest positive integer that can be generated
    # So, for a query K, we count the number of subarrays whose gcd is a divisor of K
    # But since K can be up to 1e6, we can precompute for all possible K up to 1e6
    
    # We'll use a frequency array to count how many subarrays have a particular gcd
    max_k = 10**6
    freq = [0] * (max_k + 1)
    
    # For each starting index i, we'll track the gcd of the subarray starting at i
    # We'll use a list to store the current gcds as we extend the subarray
    # This is similar to the approach used in the problem of finding the number of subarrays with a given gcd
    
    for i in range(N):
        current_gcd = 0
        for j in range(i, N):
            current_gcd = math.gcd(current_gcd, A[j])
            if current_gcd == 0:
                current_gcd = A[j]
            freq[current_gcd] += 1
    
    # For each query K, we need to count the number of subarrays whose gcd divides K
    # We can do this by checking all divisors of K and summing their frequencies
    # To find the divisors of K efficiently, we can precompute them for all K up to 1e6
    
    # Precompute divisors for all K up to 1e6
    divisors = [[] for _ in range(max_k + 1)]
    for i in range(1, max_k + 1):
        for j in range(i, max_k + 1, i):
            divisors[j].append(i)
    
    # Process queries
    for K in queries:
        res = 0
        for d in divisors[K]:
            res += freq[d]
        print(res)

if __name__ == '__main__':
    solve()