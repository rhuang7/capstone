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
        
        # Preprocess: create a map from number to list of positions
        pos_map = defaultdict(list)
        for i, num in enumerate(wheel):
            pos_map[num].append(i)
        
        # For each query, find the minimum number of coins
        for K in queries:
            positions = pos_map[K]
            min_coins = float('inf')
            # Try all possible starting positions
            for start in positions:
                # Try both directions
                # Direction 1: clockwise (increasing index)
                # Direction 2: counter-clockwise (decreasing index)
                # Find the minimum distance between any two positions
                # Since the wheel is circular, the distance between two positions is min(|a - b|, N - |a - b|)
                # We need to find the minimum distance between any two positions in the list
                # Since the wheel is circular, the minimal distance between any two positions is the minimum of the distances between all pairs
                # But since we can start at any position and spin in either direction, the minimal number of coins is the minimal distance between any two positions in the list
                # Because the needle can start at any of the K positions and spin in either direction
                # So the minimal coins is the minimal distance between any two positions in the list
                # Since the wheel is circular, the minimal distance between any two positions is the minimum of the distances between all pairs
                # But since we can choose any starting position and any direction, the minimal coins is the minimal distance between any two positions in the list
                # So we can compute the minimal distance between any two positions in the list
                # For each position, compute the minimal distance to any other position
                for end in positions:
                    if start == end:
                        continue
                    dist = min(abs(start - end), N - abs(start - end))
                    if dist < min_coins:
                        min_coins = dist
            results.append(str(min_coins))
    
    print('\n'.join(results))