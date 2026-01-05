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
        
        # Precompute depths and parents for LCA
        LOG = 20
        up = [[-1]*(N+1) for _ in range(LOG)]
        depth = [0]*(N+1)
        
        # BFS to compute depth and parent[0]
        q = deque()
        q.append(1)
        up[0][1] = -1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if up[0][v] == -1 and v != up[0][u]:
                    up[0][v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        # Precompute binary lifting table
        for k in range(1, LOG):
            for v in range(1, N+1):
                if up[k-1][v] != -1:
                    up[k][v] = up[k-1][up[k-1][v]]
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u up to depth of v
            for k in range(LOG-1, -1, -1):
                if depth[u] - (1 << k) >= depth[v]:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if up[k][u] != -1 and up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]
        
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
            
            # Check if possible
            d_ab = distance(a, b)
            if abs(da - db) > d_ab or (da + db) < d_ab:
                results.append("-1")
                continue
            
            # Find possible x
            # Case 1: x is on the path from a to b
            # Case 2: x is on the path from a to lca, or from b to lca
            # We need to find x such that d(x,a) = da and d(x,b) = db
            
            # Find the lca of a and b
            l = lca(a, b)
            
            # Case 1: x is on the path from a to lca
            # Then d(x,a) = da, so x is da steps away from a towards lca
            # d(x,b) = d(a,b) - d(x,a) = d_ab - da
            # So we need db = d_ab - da
            if da + db == d_ab:
                # Check if there is a node da steps from a towards lca
                # Move a up da steps towards lca
                x = a
                for _ in range(da):
                    x = up[0][x]
                if x != -1 and distance(x, b) == db:
                    results.append(str(x))
                    continue
            
            # Case 2: x is on the path from b to lca
            # Then d(x,b) = db, so x is db steps away from b towards lca
            # d(x,a) = d(a,b) - db = da
            if db + da == d_ab:
                # Check if there is a node db steps from b towards lca
                x = b
                for _ in range(db):
                    x = up[0][x]
                if x != -1 and distance(x, a) == da:
                    results.append(str(x))
                    continue
            
            # Case 3: x is on the path from a to lca, but not directly
            # We need to find x such that d(x,a) = da and d(x,b) = db
            # This is more complex, but since the tree is a tree, there is at most one such x
            # So we can try to find it by checking the two possible paths
            # Try moving a up da steps and check if it satisfies
            x = a
            for _ in range(da):
                x = up[0][x]
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving b up db steps and check if it satisfies
            x = b
            for _ in range(db):
                x = up[0][x]
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, return -1
            results.append("-1")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()