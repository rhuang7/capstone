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
            max_val = max(max_val, num)
        
        # Use a sieve-like approach to count multiples
        cnt = [0] * (max_val + 1)
        for num in A:
            for multiple in range(num, max_val + 1, num):
                cnt[multiple] += 1
        
        # Now calculate star values
        for num in A:
            star = 0
            for multiple in range(num, max_val + 1, num):
                star += cnt[multiple]
            max_star = max(max_star, star)
        
        results.append(str(max_star))
    
    print('\n'.join(results))