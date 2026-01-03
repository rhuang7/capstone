import sys
import math
from collections import deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    # Build tree
    tree = [[] for _ in range(N)]
    for i in range(0, len(edges), 2):
        u = int(edges[i]) - 1
        v = int(edges[i+1]) - 1
        tree[u].append(v)
        tree[v].append(u)
    
    # BFS to find depth of each node
    depth = [0] * N
    visited = [False] * N
    q = deque()
    q.append(0)
    visited[0] = True
    while q:
        u = q.popleft()
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                q.append(v)
    
    # Calculate Grundy numbers
    grundy = [0] * N
    for i in range(N-1, -1, -1):
        if depth[i] == 0:
            continue
        g = 0
        for neighbor in tree[i]:
            if depth[neighbor] == depth[i] - 1:
                g ^= grundy[neighbor]
        grundy[i] = g
    
    # Total XOR of all non-capital nodes
    total_xor = 0
    for i in range(1, N):
        total_xor ^= grundy[i] ^ S[i]
    
    if total_xor != 0:
        print("First")
    else:
        print("Second")