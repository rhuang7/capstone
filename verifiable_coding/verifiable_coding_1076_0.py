import sys
import math
from collections import deque, defaultdict

input = sys.stdin.buffer.read
def solve():
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
        depth = [0] * (N+1)
        parent = [[-1] * (N+1) for _ in range(LOG)]
        
        # BFS to compute depth and parent[0]
        q = deque()
        q.append(1)
        visited = [False] * (N+1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[0][v] = u
                    q.append(v)
        
        # Fill parent table
        for k in range(1, LOG):
            for v in range(1, N+1):
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
        
        # Function to get distance between two nodes
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
            
            # Check if a and b are valid
            if da + db < distance(a, b):
                results.append("-1")
                continue
            if da + db > distance(a, b):
                results.append("-1")
                continue
            
            # Find possible x
            # Case 1: x is on the path from a to lca(a, b)
            l = lca(a, b)
            # Check if there is a node x such that d(x, a) = da and d(x, b) = db
            # x must be on the path from a to lca(a, b) or from b to lca(a, b)
            # So we check both possibilities
            
            # Check path from a to lca(a, b)
            # The distance from a to lca is d_a_lca = depth[a] - depth[l]
            # So the node x must be at distance da from a, which is along the path from a to lca
            # So the distance from x to lca is da - d_a_lca
            # Similarly for b
            d_a_lca = depth[a] - depth[l]
            d_b_lca = depth[b] - depth[l]
            
            # Check if x is on the path from a to lca
            if da <= d_a_lca and db <= d_b_lca:
                # x is on the path from a to lca
                # move da steps from a towards lca
                x = a
                for _ in range(da):
                    x = parent[0][x]
                # check if distance from x to b is db
                if distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Check path from b to lca
            if da <= d_a_lca and db <= d_b_lca:
                # x is on the path from b to lca
                x = b
                for _ in range(db):
                    x = parent[0][x]
                # check if distance from x to a is da
                if distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            # Check path from lca to a
            if da <= d_a_lca and db <= d_b_lca:
                # x is on the path from lca to a
                x = l
                for _ in range(da):
                    x = parent[0][x]
                # check if distance from x to b is db
                if distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Check path from lca to b
            if da <= d_a_lca and db <= d_b_lca:
                x = l
                for _ in range(db):
                    x = parent[0][x]
                # check if distance from x to a is da
                if distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            # Check if x is on the path from a to b
            # The distance from a to b is d_ab = distance(a, b)
            # The distance from x to a is da, from x to b is db
            # So x must be at distance da from a and db from b
            # So x must be on the path from a to b
            # So we check if there is a node x such that distance(x, a) = da and distance(x, b) = db
            # The distance from a to b is d_ab = distance(a, b)
            # So da + db = d_ab
            # So x is at distance da from a towards b
            d_ab = distance(a, b)
            if da + db == d_ab:
                x = a
                for _ in range(da):
                    x = parent[0][x]
                if distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Check if x is on the path from b to a
            if da + db == d_ab:
                x = b
                for _ in range(db):
                    x = parent[0][x]
                if distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            # If none of the above, return -1
            results.append("-1")
    
    print("\n".join(results))