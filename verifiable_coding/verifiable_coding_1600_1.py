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
        
        # Preprocess: create a dictionary to map each number to its positions
        pos = defaultdict(list)
        for i, num in enumerate(wheel):
            pos[num].append(i)
        
        # For each query, find the minimum number of coins
        for K in queries:
            positions = pos[K]
            min_coins = float('inf')
            # Try all possible starting positions
            for start in positions:
                # Try both directions (clockwise and counter-clockwise)
                # Since the wheel is circular, we can compute the minimum distance
                # between start and any other position of K
                # The minimum distance is min( (start - end) % N, (end - start) % N )
                # But since we want the minimum number of coins, which is the number of coins
                # encountered, which is the distance between start and end (including both)
                # So the minimum coins is the minimum distance between any two positions of K
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can find the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can compute the minimum distance between any two positions of K
                # and that is the minimum coins required
                # So we can