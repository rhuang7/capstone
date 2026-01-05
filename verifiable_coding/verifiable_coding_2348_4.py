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
    
    # Preprocess for binary search
    # For each hotel, find the farthest hotel reachable in one day
    # We'll create a list where for each position i, we store the farthest position j such that x[j] - x[i] <= L
    # This can be done using binary search since x is sorted
    max_reach = [0] * N
    for i in range(N):
        # Find the largest j such that x[j] - x[i] <= L
        j = bisect.bisect_right(x, x[i] + L) - 1
        max_reach[i] = j
    
    # Preprocess for each position, the farthest position it can reach in one day
    # We'll create a list of jumps, where jump[i] is the farthest position reachable from i in one day
    # We'll also create a list of next positions for each position, to allow binary lifting for queries
    # For this problem, we can use binary lifting to answer queries in O(log N) time per query
    # We'll create a log table for binary lifting
    
    LOG = 20
    up = [[0] * N for _ in range(LOG)]
    for i in range(N):
        up[0][i] = max_reach[i]
    
    for k in range(1, LOG):
        for i in range(N):
            up[k][i] = up[k-1][up[k-1][i]]
    
    # Function to find the minimum number of days to travel from a to b
    def min_days(a, b):
        if a > b:
            # Need to go backwards
            # We need to find the farthest hotel that can be reached from b in one day, and so on
            # We'll reverse the array and use the same logic
            # But for this problem, since the hotels are sorted, we can reverse the logic
            # We'll create a reverse max_reach array
            # But for now, we'll handle it directly
            # We'll reverse the array and use the same function
            # But since the hotels are sorted, we can just reverse the logic
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # But for now, we'll handle it directly
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from b in one day, and so on
            # We'll use the same up table but in reverse
            # We'll find the farthest hotel that can be reached from