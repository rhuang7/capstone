import sys
import math
from collections import defaultdict, deque

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
        
        # Find the node with the minimum W
        min_w = float('inf')
        best_x = 1
        
        for u in range(1, N + 1):
            # When u is removed, the tree splits into several components
            # The number of components is the number of children of u (excluding parent)
            # The size of each component is the size of the subtree rooted at each child
            # The maximum size among these is the W for removing u
            # Also, the parent component is N - size[u]
            # So W is max(max_child_size, N - size[u])
            max_child_size = 0
            for v in tree[u]:
                if v != 1:  # assuming 1 is the root, but we need to check all possible parents
                    max_child_size = max(max_child_size, size[v])
            w = max(max_child_size, N - size[u])
            if w < min_w or (w == min_w and u < best_x):
                min_w = w
                best_x = u
        
        results.append(f"{best_x} {min_w}")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()