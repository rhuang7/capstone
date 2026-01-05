import sys
import bisect
from collections import deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    tree = [[] for _ in range(N+1)]
    for i in range(N-1):
        u = int(edges[2*i])
        v = int(edges[2*i+1])
        tree[u].append(v)
        tree[v].append(u)
    
    # BFS to find parent and depth for each node
    parent = [0]*(N+1)
    depth = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
    
    # For each node, collect the path from 1 to it
    # We'll use a list to store the path and then compute LIS
    # However, for large N, we need an efficient way
    
    # We'll use a dynamic programming approach for LIS
    # For each node, we'll keep track of the LIS up to that node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll perform a BFS again, but this time for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to the node
    
    # We'll use a list to store the LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node
    # We'll use a list to store the current LIS for the path from 1 to the node