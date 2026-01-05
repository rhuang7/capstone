import sys
import sys
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        tree = defaultdict(list)
        for _ in range(N - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Compute sizes of subtrees
        size = [0] * (N + 1)
        def dfs(u, parent):
            size[u] = 1
            for v in tree[u]:
                if v != parent:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(1, -1)
        
        # Find the node with the smallest maximum subtree size
        min_w = float('inf')
        best_x = 1
        
        for u in range(1, N + 1):
            w = 0
            for v in tree[u]:
                if size[v] > 0:
                    w = max(w, size[v])
            if w < min_w or (w == min_w and u < best_x):
                min_w = w
                best_x = u
        
        results.append(f"{best_x} {min_w}")
    
    print("\n".join(results))