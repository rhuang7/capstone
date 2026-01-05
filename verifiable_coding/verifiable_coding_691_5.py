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
        
        # Sieve of Eratosthenes-like approach to count multiples
        cnt = [0] * (max_val + 1)
        for num in A:
            cnt[num] += 1
        
        for i in range(1, max_val + 1):
            for j in range(2 * i, max_val + 1, i):
                cnt[i] += cnt[j]
        
        for num in A:
            max_star = max(max_star, cnt[num])
        
        results.append(str(max_star))
    
    print('\n'.join(results))