import sys
import bisect
from collections import deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    adj = [[] for _ in range(N+1)]
    for i in range(N-1):
        u = int(edges[2*i])
        v = int(edges[2*i+1])
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to find parent and depth of each node
    parent = [0]*(N+1)
    depth = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    parent[1] = 0
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
    
    # For each node, store the path from root to it
    path = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        current = i
        path[i] = []
        while current != 0:
            path[i].append(a[current-1])
            current = parent[current]
        path[i] = path[i][::-1]  # reverse to get correct order
    
    # For each path, compute LIS
    result = [0]*(N+1)
    for k in range(1, N+1):
        seq = path[k]
        lis = []
        for num in seq:
            idx = bisect.bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
        result[k] = len(lis)
    
    for k in range(1, N+1):
        print(result[k])

if __name__ == '__main__':
    solve()