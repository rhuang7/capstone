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
    
    # Compute distance from capital (node 0)
    distance = [0] * N
    visited = [False] * N
    q = deque()
    q.append(0)
    visited[0] = True
    while q:
        u = q.popleft()
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                q.append(v)
    
    # Compute Grundy numbers (nimber) for each node
    grundy = [0] * N
    for i in range(N):
        if distance[i] == 0:
            continue
        # Move soldiers from node i to its parent
        # The number of soldiers is S[i]
        # The grundy number for this move is the grundy of the parent
        grundy[i] = grundy[tree[0][0]] if distance[i] == 1 else grundy[tree[i][0]]
    
    # Total XOR of all grundy numbers
    total_xor = 0
    for i in range(N):
        total_xor ^= grundy[i]
    
    if total_xor != 0:
        print("First")
    else:
        print("Second")