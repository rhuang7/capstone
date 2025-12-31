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
    # For each hotel, precompute the farthest hotel reachable in one day
    # Using binary search
    next_pos = [0] * N
    for i in range(N-1, -1, -1):
        if i == N-1:
            next_pos[i] = i
        else:
            # Find the farthest hotel that is within L distance
            # Start from i+1 and find the farthest j such that pos[j] - pos[i] <= L
            # Since pos is sorted, we can use binary search
            max_j = bisect.bisect_right(pos, pos[i] + L) - 1
            next_pos[i] = min(max_j, N-1)
    
    # Precompute for each hotel, the farthest hotel it can reach in one day
    # Now, for each query, we need to find the minimum number of days
    # This can be done using binary lifting or BFS, but with Q up to 1e5 and N up to 1e5, we need an efficient method
    
    # We will use binary lifting for each hotel, precomputing 2^k steps
    # Precompute log2(N) levels
    LOG = 20
    up = [[0]*LOG for _ in range(N)]
    
    # Fill up[0] with next_pos
    for i in range(N):
        up[i][0] = next_pos[i]
    
    # Fill up for higher levels
    for k in range(1, LOG):
        for i in range(N):
            up[i][k] = up[up[i][k-1]][k-1]
    
    # Function to find the minimum number of days from a to b
    def min_days(a, b):
        if a == b:
            return 0
        # Ensure a < b
        if a > b:
            a, b = b, a
        days = 0
        # Jump as far as possible
        for k in range(LOG-1, -1, -1):
            if up[a][k] <= b:
                days += 1
                a = up[a][k]
                if a == b:
                    return days
        return days
    
    # Process queries
    for a, b in queries:
        print(min_days(a, b))

if __name__ == '__main__':
    solve()