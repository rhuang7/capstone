import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    x = list(map(int, data[idx:idx+N]))
    idx += N
    L = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        a = int(data[idx]) - 1
        b = int(data[idx+1]) - 1
        queries.append((a, b))
        idx += 2
    
    # Preprocess the positions
    pos = x
    # For each position, store the index
    # We'll use binary search to find the farthest hotel within L distance
    # We'll build a list of positions and use binary search to find the farthest reachable hotel
    
    # Precompute for each hotel, the farthest hotel it can reach in one day
    # We'll use binary search for each query
    # For a given start position, find the farthest hotel that is within L distance
    # Since the hotels are sorted, we can use binary search
    
    # Precompute the positions
    # For each hotel, find the farthest hotel it can reach in one day
    # We'll use binary search for this
    
    # Function to find the farthest hotel reachable from a given hotel in one day
    def find_farthest(start):
        left = start + 1
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if pos[mid] - pos[start] <= L:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    # Precompute the farthest hotel for each hotel
    farthest = [0] * N
    for i in range(N):
        farthest[i] = find_farthest(i)
    
    # Now, for each query, we need to find the minimum number of days
    # We can use binary lifting or BFS for each query, but with Q up to 1e5, we need an efficient approach
    
    # We'll use binary lifting to precompute jumps of 2^k steps
    # Precompute log2(N) levels
    LOG = 20
    up = [[0] * LOG for _ in range(N)]
    
    # Initialize the up table
    for i in range(N):
        up[i][0] = farthest[i]
    
    # Fill the up table
    for k in range(1, LOG):
        for i in range(N):
            up[i][k] = up[up[i][k-1]][k-1]
    
    # Function to find the minimum number of days to reach from a to b
    def min_days(a, b):
        if a > b:
            a, b = b, a
        res = 0
        for k in reversed(range(LOG)):
            if up[a][k] >= b:
                res += 1
                a = up[a][k]
                if a == b:
                    return res
        return -1  # Should not happen as per problem statement
    
    # Process queries
    for a, b in queries:
        print(min_days(a, b))
    
if __name__ == '__main__':
    solve()