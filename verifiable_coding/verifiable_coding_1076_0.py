import sys
import math
from sys import stdin
import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        
        # Build adjacency list
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Precompute depth and parent for LCA
        LOG = 20
        depth = [0] * (N + 1)
        parent = [[-1] * (N + 1) for _ in range(LOG)]
        
        # BFS to compute depth and parent[0]
        from collections import deque
        q = deque()
        q.append(1)
        visited = [False] * (N + 1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    q.append(v)
        
        # Precompute parent table
        for k in range(1, LOG):
            for v in range(1, N + 1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u up to the depth of v
            for k in range(LOG-1, -1, -1):
                if depth[u] - (1 << k) >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        
        # Function to find the k-th ancestor of a node
        def get_kth_ancestor(u, k):
            for i in range(LOG):
                if k & (1 << i):
                    u = parent[i][u]
                    if u == -1:
                        return -1
            return u
        
        # Function to find the distance between two nodes
        def distance(u, v):
            ancestor = lca(u, v)
            return depth[u] + depth[v] - 2 * depth[ancestor]
        
        # Process queries
        for _ in range(Q):
            a = int(data[idx])
            da = int(data[idx+1])
            b = int(data[idx+2])
            db = int(data[idx+3])
            idx += 4
            
            # Check if the distances are possible
            d_ab = distance(a, b)
            if abs(da - db) > d_ab or da + db < d_ab:
                results.append("-1")
                continue
            
            # Find the possible nodes
            # Case 1: x is on the path from a to lca(a,b)
            # Case 2: x is on the path from b to lca(a,b)
            l = lca(a, b)
            # Move a up by da steps
            x1 = get_kth_ancestor(a, da)
            if x1 != -1 and distance(x1, b) == db:
                results.append(str(x1))
                continue
            
            # Move b up by db steps
            x2 = get_kth_ancestor(b, db)
            if x2 != -1 and distance(x2, a) == da:
                results.append(str(x2))
                continue
            
            # Check if there is a node on the path from a to lca(a,b) that is da steps away from a and db steps away from b
            # This is possible only if the distance from a to lca is >= da and the distance from lca to b is >= db - da
            # Similarly for the other direction
            # Case 1: x is on the path from a to lca
            if depth[a] >= da and depth[b] - depth[l] >= db - da:
                x = get_kth_ancestor(a, da)
                if distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Case 2: x is on the path from b to lca
            if depth[b] >= db and depth[a] - depth[l] >= da - db:
                x = get_kth_ancestor(b, db)
                if distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            # If none of the above, check if there is a node on the path from lca to a that is da steps away from a and db steps away from b
            # This is possible only if the distance from a to lca is >= da and the distance from lca to b is >= db - da
            # Similarly for the other direction
            # Case 1: x is on the path from a to lca
            if depth[a] >= da and depth[b] - depth[l] >= db - da:
                x = get_kth_ancestor(a, da)
                if distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Case 2: x is on the path from b to lca
            if depth[b] >= db and depth[a] - depth[l] >= da - db:
                x = get_kth_ancestor(b, db)
                if distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            # If none of the above, check if there is a node on the path from lca to a that is da steps away from a and db steps away from b
            # This is possible only if the distance from a to lca is >= da and the distance from lca to b is >= db - da
            # Similarly for the other direction
            # Case 1: x is on the path from a to lca
            if depth[a] >= da and depth[b] - depth[l] >= db - da:
                x = get_kth_ancestor(a, da)
                if distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Case 2: x is on the path from b to lca
            if depth[b] >= db and depth[a] - depth[l] >= da - db:
                x = get_kth_ancestor(b, db)
                if distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            results.append("-1")
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()