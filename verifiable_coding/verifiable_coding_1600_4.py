import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        wheel = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        queries = list(map(int, data[idx:idx+Q]))
        idx += Q
        
        # Create a dictionary to map each number to its positions
        pos = collections.defaultdict(list)
        for i, num in enumerate(wheel):
            pos[num].append(i)
        
        # Precompute the minimum coins for each number
        min_coins = {}
        for num in pos:
            positions = pos[num]
            min_dist = float('inf')
            # Check all possible starting positions
            for i in range(len(positions)):
                # Try both directions
                # Clockwise: (positions[i] + 1) % N, (positions[i] + 2) % N, ...
                # Counter-clockwise: (positions[i] - 1) % N, (positions[i] - 2) % N, ...
                # Find the minimum distance to another occurrence of num
                for j in range(1, len(positions)):
                    dist = abs(positions[i] - positions[j])
                    if dist > N // 2:
                        dist = N - dist
                    min_dist = min(min_dist, dist)
            min_coins[num] = min_dist
        
        # Process each query
        for K in queries:
            print(min_coins[K])