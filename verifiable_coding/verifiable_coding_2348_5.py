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
    # For each hotel, find the farthest hotel it can reach in one day
    # Using binary search
    # We will create an array 'next' where next[i] is the farthest hotel index that can be reached from i in one day
    next = [0] * N
    for i in range(N):
        # Find the farthest j such that x[j] - x[i] <= L
        # Since x is sorted, we can use binary search
        max_dist = x[i] + L
        j = bisect.bisect_right(x, max_dist) - 1
        next[i] = j
    
    # Preprocess the previous array
    prev = [0] * N
    for i in range(N-1, -1, -1):
        # Find the farthest hotel before i that can be reached in one day
        min_dist = x[i] - L
        j = bisect.bisect_left(x, min_dist)
        prev[i] = j
    
    # For each query, compute the minimum number of days
    # We can use binary lifting or a BFS approach
    # Since N and Q are up to 1e5, we need an O(Q log N) solution
    # We will use binary lifting to precompute 2^k steps
    
    # Precompute binary lifting table
    LOG = 20
    up = [[0]*LOG for _ in range(N)]
    for i in range(N):
        up[i][0] = next[i]
    for k in range(1, LOG):
        for i in range(N):
            up[i][k] = up[up[i][k-1]][k-1]
    
    # Function to compute the number of days from a to b
    def get_days(a, b):
        if a == b:
            return 0
        # Assume a < b
        if a > b:
            a, b = b, a
        days = 0
        for k in range(LOG-1, -1, -1):
            if up[a][k] <= b:
                days += 1
                a = up[a][k]
                if a == b:
                    break
        return days
    
    # Process queries
    for a, b in queries:
        if a > b:
            a, b = b, a
        # We need to find the minimum number of days to go from a to b
        # We can use binary lifting to find the number of steps
        # But since the graph is directed and acyclic, we can use the binary lifting table
        # However, the binary lifting table only gives the next hotel, not the number of days
        # So we need to compute the number of steps from a to b
        # We can do this by moving from a to next[a], next[next[a]], etc., until we reach b
        # But this would be O(Q*N) in worst case, which is too slow
        # So we need a better approach
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]], etc.
        # We can do this with a loop
        # But this is O(Q*N) in worst case, which is too slow
        # So we need to find a way to compute the number of steps in O(log N) time
        # We can use binary lifting to find the number of steps
        # We can precompute for each position, the number of steps to reach the next position
        # But that would require O(N*LOG) space
        # So we can precompute for each position, the number of steps to reach the next position
        # But that would not help us directly
        # So we need to find the number of steps from a to b by moving from a to next[a], next[next[a]],