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
    
    # Build the tree
    tree = [[] for _ in range(N)]
    for i in range(0, len(edges), 2):
        u = int(edges[i]) - 1
        v = int(edges[i+1]) - 1
        tree[u].append(v)
        tree[v].append(u)
    
    # Compute the depth of each node and the distance from the capital
    depth = [0] * N
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
                depth[v] = depth[u] + 1
                distance[v] = distance[u] + 1
                q.append(v)
    
    # Calculate the total number of soldiers at each level
    level_s = [0] * (N)
    for i in range(1, N):
        level_s[distance[i]] += S[i]
    
    # Game is equivalent to Nim game with piles of size level_s[i]
    # The Grundy number for each pile is its size
    # The XOR of all piles determines the winner
    xor_sum = 0
    for i in range(N):
        xor_sum ^= level_s[i]
    
    if xor_sum != 0:
        print("First")
    else:
        print("Second")