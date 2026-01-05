import sys
import bisect

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(N-1):
        u = int(edges[2*i])
        v = int(edges[2*i+1])
        graph[u].append(v)
        graph[v].append(u)
    
    # For each node, store the path from 1 to it
    # We'll use BFS to find the shortest path
    from collections import deque
    parent = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
    
    # Now, for each node, reconstruct the path from 1 to it
    # We'll use a list to store the path for each node
    path = [[] for _ in range(N+1)]
    for k in range(1, N+1):
        current = k
        while current != 0:
            path[k].append(current)
            current = parent[current]
        path[k] = path[k][::-1]
    
    # Now, for each path, compute the LIS
    # We'll use a list to store the LIS for each path
    lis = [0]*(N+1)
    
    for k in range(1, N+1):
        seq = [a[i-1] for i in path[k]]
        # Compute LIS for seq
        dp = []
        for num in seq:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        lis[k] = len(dp)
    
    for k in range(1, N+1):
        print(lis[k])

if __name__ == '__main__':
    solve()