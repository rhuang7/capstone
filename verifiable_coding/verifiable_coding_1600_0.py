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
        wheel = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        queries = list(map(int, data[idx:idx+Q]))
        idx += Q
        
        pos = defaultdict(list)
        for i, num in enumerate(wheel):
            pos[num].append(i)
        
        for K in queries:
            positions = pos[K]
            min_coins = float('inf')
            for i in range(len(positions)):
                start = positions[i]
                for j in range(i, len(positions)):
                    end = positions[j]
                    if start == end:
                        coins = 1
                    else:
                        coins = (end - start + 1) * 2 - 1
                    min_coins = min(min_coins, coins)
            results.append(str(min_coins))
    
    print('\n'.join(results))