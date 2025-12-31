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
    
    # Compute depth and parent for each node
    depth = [0] * N
    parent = [ -1 ] * N
    visited = [False] * N
    q = deque()
    q.append(0)
    visited[0] = True
    while q:
        u = q.popleft()
        for v in tree[u]:
            if not visited[v] and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                visited[v] = True
                q.append(v)
    
    # Compute the Grundy number for each node
    grundy = [0] * N
    for i in range(N-1, -1, -1):
        if i == 0:
            grundy[i] = 0
        else:
            grundy[i] = grundy[parent[i]] ^ S[i]
    
    # Calculate the XOR of all grundy numbers
    total_xor = 0
    for i in range(N):
        total_xor ^= grundy[i]
    
    if total_xor != 0:
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    solve()