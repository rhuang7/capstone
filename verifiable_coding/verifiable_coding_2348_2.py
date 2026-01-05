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
    reach = [0] * N
    for i in range(N):
        # Find the farthest hotel j such that x[j] - x[i] <= L
        # Since x is sorted, we can use binary search
        max_reach = x[i] + L
        j = bisect.bisect_right(x, max_reach) - 1
        reach[i] = j
    
    # Precompute the minimum number of days between any two hotels
    # Using binary lifting
    LOG = 20
    up = [[0]*N for _ in range(LOG)]
    for i in range(N):
        up[0][i] = reach[i]
    
    for k in range(1, LOG):
        for i in range(N):
            up[k][i] = up[k-1][up[k-1][i]]
    
    def get_days(a, b):
        if a > b:
            a, b = b, a
        days = 0
        while a < b:
            days += 1
            a = up[0][a]
        return days
    
    for a, b in queries:
        print(get_days(a, b))

if __name__ == '__main__':
    solve()