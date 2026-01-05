import sys
import sys
from sys import stdin
import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Compute sizes of subtrees
        size = [0] * (N + 1)
        def dfs(u, parent):
            size[u] = 1
            for v in adj[u]:
                if v != parent:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(1, -1)
        
        # Compute the optimal node to remove
        # W is the maximum of the two largest subtree sizes
        # We need to find the node with the minimum W
        min_w = float('inf')
        best_x = 1
        
        def get_max_subtree_size(u, parent):
            max_size = 0
            for v in adj[u]:
                if v != parent:
                    if size[v] > max_size:
                        max_size = size[v]
            return max_size
        
        for u in range(1, N + 1):
            # When we remove u, the tree is split into components
            # The sizes of the components are the sizes of the subtrees of u's children
            # And the rest of the tree (N - size[u])
            max_size = 0
            for v in adj[u]:
                if size[v] > max_size:
                    max_size = size[v]
            # The other component is N - size[u]
            if (N - size[u]) > max_size:
                max_size = N - size[u]
            # W is the maximum of the two largest components
            W = max_size
            if W < min_w or (W == min_w and u < best_x):
                min_w = W
                best_x = u
        
        results.append(f"{best_x} {min_w}")
    
    print("\n".join(results))

if __name__ == '__main__':
    main()