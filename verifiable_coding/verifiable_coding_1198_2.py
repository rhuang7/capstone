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
    
    # Precompute prefix sums and gcds
    prefix_gcd = []
    current_gcd = 0
    for num in A:
        current_gcd = math.gcd(current_gcd, num)
        prefix_gcd.append(current_gcd)
    
    # For each query K, count the number of subarrays that can generate K
    # A subarray [l..r] can generate K if and only if the gcd of the subarray is a divisor of K
    # And the sum of the subarray is divisible by the gcd
    # But since we are only interested in whether K can be generated, we can check if K is divisible by the gcd of the subarray
    
    # Precompute for each position the gcd of the subarray ending at that position
    # And for each possible gcd, store the positions where it occurs
    gcd_positions = defaultdict(list)
    current_gcd = 0
    for i in range(N):
        current_gcd = math.gcd(current_gcd, A[i])
        gcd_positions[current_gcd].append(i)
    
    # For each query K, iterate over all possible divisors of K
    # And for each divisor d, check how many subarrays have gcd equal to d and K is divisible by d
    # But since K can be up to 1e6, we can precompute for each d up to 1e6, the count of subarrays with gcd d
    # Then for each query K, iterate over all divisors of K and sum the counts
    
    # Precompute for each d up to 1e6, the count of subarrays with gcd d
    max_k = 10**6
    count_gcd = [0] * (max_k + 1)
    
    # For each position, we track the current gcd of subarrays ending at that position
    # And for each gcd, we update the count
    current_gcd = 0
    for i in range(N):
        current_gcd = math.gcd(current_gcd, A[i])
        count_gcd[current_gcd] += 1
    
    # Now, for each query K, find all divisors of K and sum count_gcd[d] for each divisor d of K
    # But we need to make sure that K is divisible by d, so d must be a divisor of K
    
    # Precompute divisors for all numbers up to 1e6
    divisors = [[] for _ in range(max_k + 1)]
    for i in range(1, max_k + 1):
        for j in range(i, max_k + 1, i):
            divisors[j].append(i)
    
    # Now process each query
    for K in queries:
        res = 0
        for d in divisors[K]:
            res += count_gcd[d]
        print(res)
    
if __name__ == '__main__':
    solve()