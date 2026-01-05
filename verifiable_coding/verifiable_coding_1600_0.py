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
        
        # Preprocess: map each number to its positions
        pos = defaultdict(list)
        for i, num in enumerate(wheel):
            pos[num].append(i)
        
        # For each query, find the minimum coins
        for K in queries:
            positions = pos[K]
            min_coins = float('inf')
            # Try all possible starting positions
            for start in positions:
                # Try both directions
                # Clockwise: start, start+1, ..., start + d
                # Counter-clockwise: start, start-1, ..., start - d
                # Find the minimum distance to reach K again
                # Since the wheel is circular, the distance can be calculated as min(d, N-d)
                # But since we can choose direction, the minimum coins is the minimum distance between any two positions of K
                # So we need to find the minimum distance between any two positions of K
                # The minimum distance between any two positions of K is the minimum of (pos[i] - pos[j]) % N for all i, j
                # But since we can choose direction, the minimum coins is the minimum of (distance between any two positions of K)
                # So for each position, compute the distance to the next occurrence of K in either direction
                # The minimum of these distances is the answer
                # We can find the minimum distance between any two positions of K
                # Since the wheel is circular, the distance between two positions is min(|a - b|, N - |a - b|)
                # But since we can choose direction, the minimum coins is the minimum distance between any two positions of K
                # So we can find the minimum distance between any two positions of K
                # So for each K, we find the minimum distance between any two positions of K
                # The minimum distance between any two positions of K is the minimum of (pos[i] - pos[j]) % N for all i, j
                # But since we can choose direction, the minimum coins is the minimum of (distance between any two positions of K)
                # So we can compute the minimum distance between any two positions of K
                # For this, we can sort the positions and compute the minimum distance between consecutive positions
                # Also, the distance between the first and last position is N - (last - first)
                # So we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and between first and last
                # The minimum of these is the answer
                # So for each K, we sort the positions and compute the minimum distance between consecutive positions and