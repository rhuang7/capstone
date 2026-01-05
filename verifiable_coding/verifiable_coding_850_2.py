import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute frequency of each number
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        
        # Compute all possible GCDs of subsets
        gcds = set()
        for num in A:
            current_gcd = num
            for i in range(1, N):
                current_gcd = math.gcd(current_gcd, A[i])
                gcds.add(current_gcd)
        
        # Find the maximum sum of two distinct GCDs
        max_sum = 0
        for g in gcds:
            for h in gcds:
                if g != h:
                    max_sum = max(max_sum, g + h)
        
        results.append(str(max_sum))
    
    print('\n'.join(results))