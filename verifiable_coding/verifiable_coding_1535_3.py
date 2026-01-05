import sys
import math
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
        
        # Compute size of each subtree
        size = [1] * (N + 1)
        visited = [False] * (N + 1)
        
        def dfs(u, parent):
            visited[u] = True
            for v in tree[u]:
                if not visited[v]:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(1, -1)
        
        # Find the node with the smallest W
        min_w = float('inf')
        best_x = 1
        
        for u in range(1, N + 1):
            # If we remove u, the tree splits into several subtrees
            # The number of fighters is the maximum size of these subtrees
            # The number of subtrees is the number of children of u
            # But we need to consider the parent side as well
            # So the number of subtrees is the number of children of u
            # The sizes of these subtrees are size[v] for each child v
            # Also, the parent side has size[N+1 - size[u]]
            # So the maximum size among these is the W for removing u
            # So we need to find the maximum size of the subtrees when u is removed
            # The maximum size is the maximum of the sizes of the children of u and (N + 1 - size[u])
            max_subtree = 0
            for v in tree[u]:
                if v != 1:  # not the parent
                    max_subtree = max(max_subtree, size[v])
            max_subtree = max(max_subtree, N + 1 - size[u])
            if max_subtree < min_w:
                min_w = max_subtree
                best_x = u
            elif max_subtree == min_w and u < best_x:
                best_x = u
        
        results.append(f"{best_x} {min_w}")
    
    print("\n".join(results))