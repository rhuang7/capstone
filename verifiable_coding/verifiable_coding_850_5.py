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
        
        if N == 2:
            results.append(str(max(A) + min(A)))
            continue
        
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        
        max_gcd = 0
        for num in A:
            if freq[num] >= 2:
                current_gcd = num
                for i in range(num-1, 0, -1):
                    if freq[i] >= 1:
                        current_gcd = i
                        break
                max_gcd = max(max_gcd, current_gcd + num)
        
        results.append(str(max_gcd))
    
    print('\n'.join(results))