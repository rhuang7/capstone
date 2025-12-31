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
    
    # Preprocess all possible subarrays and their gcds
    # For each subarray, the gcd of its elements is the smallest positive integer that can be generated
    # So for each K, we count the number of subarrays whose gcd is K
    
    # We'll use a dictionary to count the number of subarrays with each gcd
    gcd_counts = defaultdict(int)
    
    # For each starting index, track the current gcd
    current_gcd = 0
    for num in A:
        current_gcd = math.gcd(current_gcd, num)
        gcd_counts[current_gcd] += 1
    
    # For each query, output the count of subarrays with gcd equal to K
    for K in queries:
        print(gcd_counts.get(K, 0))

if __name__ == '__main__':
    solve()