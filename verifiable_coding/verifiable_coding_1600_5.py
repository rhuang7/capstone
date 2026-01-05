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
        wheel = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        queries = []
        for __ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        # Preprocess: for each number, store the indices where it appears
        pos = defaultdict(list)
        for i, num in enumerate(wheel):
            pos[num].append(i)
        
        # For each query, find the minimum number of coins
        for K in queries:
            # Get all positions of K
            positions = pos[K]
            min_coins = float('inf')
            # Try all possible starting positions
            for start in positions:
                # Try both directions (clockwise and counter-clockwise)
                # Since the wheel is circular, we can compute the minimum distance
                # between start and each occurrence of K
                # But since we can choose any starting point, we can find the minimum
                # distance between any two occurrences of K
                # The minimum number of coins is the minimum distance between any two Ks
                # But since we can choose the starting point, the minimum coins is the
                # minimum distance between any two Ks
                # So we just need to find the minimum distance between any two Ks
                # in the wheel
                # So for all pairs of positions of K, compute the distance
                # and find the minimum
                for end in positions:
                    if start == end:
                        continue
                    # Compute distance in both directions
                    dist1 = abs(end - start)
                    dist2 = N - dist1
                    min_coins = min(min_coins, min(dist1, dist2))
            results.append(str(min_coins))
    
    print('\n'.join(results))