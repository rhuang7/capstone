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
        
        # Build the tree
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Precompute depth and parent for LCA
        LOG = 20
        depth = [0] * (N + 1)
        parent = [[-1] * (N + 1) for _ in range(LOG)]
        
        # BFS to compute depth and parent[0]
        q = deque()
        q.append(1)
        depth[1] = 0
        parent[0][1] = -1
        while q:
            u = q.popleft()
            for v in tree[u]:
                if parent[0][v] == -1 and v != 1:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        # Fill the parent table
        for k in range(1, LOG):
            for v in range(1, N + 1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u to the same depth as v
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
        def kth_ancestor(u, k):
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
            
            # Check if the query is possible
            d_ab = distance(a, b)
            if abs(da - db) > d_ab or (da + db) < d_ab:
                results.append("-1")
                continue
            
            # Find possible nodes
            # Case 1: x is on the path from a to b
            # Case 2: x is on the path from a to LCA or b to LCA
            l = lca(a, b)
            # Find the node at distance da from a and db from b
            # Try moving from a towards lca
            x = kth_ancestor(a, da)
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca
            x = kth_ancestor(b, db)
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if x != -1 and distance(x, b) == db:
                results.append(str(x))
                continue
            
            # Try moving from b towards lca and then away
            x = kth_ancestor(b, db - (depth[b] - depth[l]))
            if x != -1 and distance(x, a) == da:
                results.append(str(x))
                continue
            
            # If none found, try other possibilities
            # Try moving from a towards lca and then away
            x = kth_ancestor(a, da - (depth[a] - depth[l]))
            if