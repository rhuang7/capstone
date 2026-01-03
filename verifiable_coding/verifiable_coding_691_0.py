import sys
import math
from collections import defaultdict

def solve():
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
        
        max_star = 0
        freq = defaultdict(int)
        max_val = 0
        
        for num in A:
            # Update max_val
            if num > max_val:
                max_val = num
            
            # Count multiples of num in the current frequency map
            count = 0
            for multiple in range(num, max_val + 1, num):
                count += freq[multiple]
            
            # Update max_star
            if count > max_star:
                max_star = count
            
            # Update frequency map
            freq[num] += 1
        
        results.append(str(max_star))
    
    print('\n'.join(results))