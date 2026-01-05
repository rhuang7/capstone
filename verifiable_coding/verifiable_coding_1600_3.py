import sys
import collections

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
        queries = []
        for __ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        # Preprocess: create a map from number to list of indices
        num_to_indices = collections.defaultdict(list)
        for i, num in enumerate(wheel):
            num_to_indices[num].append(i)
        
        # For each query, find the minimum coins
        for K in queries:
            indices = num_to_indices[K]
            min_coins = float('inf')
            # Try all possible starting positions
            for start in indices:
                # Try both directions (clockwise and counter-clockwise)
                # Since the wheel is circular, we can calculate the minimum distance
                # between two positions
                # For a circular array of size N, the minimum distance between start and end
                # is min(|end - start|, N - |end - start|)
                # But since we are looking for the minimum number of coins, which is the number
                # of positions the needle passes through, it's the same as the minimum distance
                # between start and any other occurrence of K
                # So for each occurrence of K, compute the minimum distance to start
                # and take the minimum of all those
                for end in indices:
                    if start == end:
                        continue
                    dist = abs(end - start)
                    min_dist = min(dist, N - dist)
                    min_coins = min(min_coins, min_dist)
            results.append(str(min_coins))
    
    print('\n'.join(results))