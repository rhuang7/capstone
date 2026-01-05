import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    edges = []
    color_dict = defaultdict(list)
    color_sum = defaultdict(int)
    color_count = defaultdict(int)
    
    for _ in range(N-1):
        a = int(data[idx]) - 1
        idx += 1
        b = int(data[idx]) - 1
        idx += 1
        c = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        edges.append((a, b, c, d))
        color_dict[c].append((a, b, d))
        color_sum[c] += d
        color_count[c] += 1
    
    for _ in range(Q):
        x = int(data[idx]) - 1
        idx += 1
        y = int(data[idx])
        idx += 1
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        
        # Build the tree with the current color values
        tree = defaultdict(list)
        for c in color_dict:
            if c != x:
                for a, b, d in color_dict[c]:
                    tree[a].append((b, d))
                    tree[b].append((a, d))
        
        # BFS to find distance between u and v
        visited = [False] * N
        q = deque()
        q.append((u, 0))
        visited[u] = True
        while q:
            node, dist = q.popleft()
            if node == v:
                print(dist)
                break
            for neighbor, d in tree[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, dist + d))