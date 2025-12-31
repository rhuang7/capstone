import sys
import bisect
from collections import deque

def solve():
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
    
    # BFS to find parent and depth for each node
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
    
    # For each node, get the path from 1 to it
    # We'll use a list to store the path for each node
    path = [[] for _ in range(N+1)]
    for k in range(1, N+1):
        current = k
        path[k] = []
        while current != 0:
            path[k].append(a[current-1])
            current = parent[current]
        path[k] = path[k][::-1]  # reverse to get the correct order
    
    # For each path, compute the length of the longest increasing subsequence
    # We'll use a list to store the LIS length for each path
    lis = [0]*N
    for k in range(1, N+1):
        seq = path[k]
        dp = [0]*len(seq)
        for i in range(len(seq)):
            idx = bisect.bisect_left(dp, seq[i])
            if idx == len(dp):
                dp.append(seq[i])
            else:
                dp[idx] = seq[i]
        lis[k-1] = len(dp)
    
    for val in lis:
        print(val)

if __name__ == '__main__':
    solve()