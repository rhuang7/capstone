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
        
        # Preprocess: map each number to its positions
        pos_map = defaultdict(list)
        for i, num in enumerate(wheel):
            pos_map[num].append(i)
        
        # For each query, find the minimum number of coins
        for K in queries:
            positions = pos_map[K]
            min_coins = float('inf')
            # Try all possible starting positions
            for start in positions:
                # Try both directions: clockwise and counter-clockwise
                # Since the wheel is circular, the distance between two positions is min(|a - b|, N - |a - b|)
                # But since we need to find the minimum number of coins, which is the number of positions visited
                # We need to find the minimal cycle length that includes all positions of K
                # The minimal cycle is the minimal distance between two positions of K
                # So we find the minimal distance between any two positions of K
                # The minimal cycle length is the minimal distance between any two positions of K
                # So for each position, find the minimal distance to another position of K
                for end in positions:
                    if start == end:
                        continue
                    dist = abs(start - end)
                    min_dist = min(dist, N - dist)
                    min_coins = min(min_coins, min_dist)
            results.append(str(min_coins))
    
    print('\n'.join(results))