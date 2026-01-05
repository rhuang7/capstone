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
    color_map = defaultdict(list)
    color_total = defaultdict(int)
    
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
        color_map[c].append((a, b, d))
        color_total[c] += d
    
    # Build adjacency list
    adj = [[] for _ in range(N)]
    for a, b, c, d in edges:
        adj[a].append((b, c, d))
        adj[b].append((a, c, d))
    
    # Precompute LCA and depth for each node
    LOG = 20
    up = [[-1]*N for _ in range(LOG)]
    depth = [0]*N
    
    def dfs(u, p):
        up[0][u] = p
        for v, c, d in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    dfs(0, -1)
    
    for k in range(1, LOG):
        for v in range(N):
            if up[k-1][v] != -1:
                up[k][v] = up[k-1][up[k-1][v]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
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
    
    def distance(u, v):
        l = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[l]
    
    # Precompute for each color the total length
    # For each query, we need to compute the distance with the color changed
    # So we need to find the path between u and v, and for each edge on the path, if its color is x_j, replace its length with y_j
    
    # We'll use a binary lifting approach to find the path between u and v
    # But since the tree is static, we can precompute for each node its parent and depth, and then find the path between u and v
    
    # For each query, we need to:
    # 1. Find the path between u and v
    # 2. For each edge on the path, if its color is x_j, replace its length with y_j
    # 3. Sum the lengths of the edges on the path
    
    # To do this efficiently, we can precompute for each color the list of edges
    # Then, for each query, we can:
    # - Find the path between u and v
    # - For each edge on the path, check if its color is x_j, and if so, replace its length with y_j
    # - Sum the lengths of the edges on the path
    
    # However, since the tree is static, we can precompute for each node its parent and depth, and then find the path between u and v
    
    # But to find the path between u and v, we need to traverse from u to LCA and from v to LCA
    
    # So for each query, we can:
    # - Find the LCA of u and v
    # - Traverse from u to LCA, collecting all edges
    # - Traverse from v to LCA, collecting all edges
    # - For each edge, if its color is x_j, replace its length with y_j
    # - Sum the lengths of the edges
    
    # However, this would be O(Q * (depth of tree)) which is O(Q * log N) since depth is O(log N) for a balanced tree
    
    # But for N up to 1e5 and Q up to 1e5, this would be O(1e10) which is too slow
    
    # Therefore, we need a more efficient approach
    
    # The key observation is that for each query, the only edges that are affected are those with color x_j
    # So for each query, we can:
    # - Find the path between u and v
    # - For each edge on the path, if its color is x_j, replace its length with y_j
    # - Sum the lengths of the edges on the path
    
    # To do this efficiently, we can precompute for each color the list of edges, and for each query, we can:
    # - For each edge on the path between u and v, check if its color is x_j, and if so, replace its length with y_j
    
    # However, this would be O(Q * (depth of tree)) which is too slow
    
    # Therefore, we need to find a way to compute the distance between u and v with the color x_j changed to y_j
    
    # The key idea is to precompute for each color the total length of all edges of that color
    # Then, for a query, we can compute the total distance between u and v as the original distance, minus the sum of the lengths of edges of color x_j on the path, plus the sum of y_j multiplied by the number of edges of color x_j on the path
    
    # But how to find the number of edges of color x_j on the path between u and v?
    
    # We can precompute for each color the list of edges, and for each query, find the number of edges of color x_j on the path between u and v
    
    # But again, this would be O(Q * (depth of tree)) which is too slow
    
    # Therefore, we need to find a way to compute for each query the number of edges of color x_j on the path between u and v
    
    # To do this, we can use a binary lifting approach to find the path between u and v, and for each edge on the path, check if its color is x_j
    
    # But this is again O(Q * (depth of tree)) which is too slow
    
    # Therefore, the only feasible approach is to precompute for each color the list of edges, and for each query, find the path between u and v, and for each edge on the path, check if its color is x_j, and if so, replace its length with y_j
    
    # So the steps are:
    # 1. Precompute for each color the list of edges
    # 2. For each query:
    #    a. Find the path between u and v
    #    b. For each edge on the path, if its color is x_j, replace its length with y_j
    #    c. Sum the lengths of the edges on the path
    
    # To find the path between u and v, we can use the LCA approach
    
    # So here's the code:
    
    for _ in range(Q):
        x = int(data[idx]) - 1
        idx += 1
        y = int(data[idx])
        idx += 1
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        
        # Find the path between u and v
        l = lca(u, v)
        path = []
        
        # Traverse from u to l
        a = u
        while a != l:
            for neighbor, c, d in adj[a]:
                if neighbor == up[0][a]:
                    path.append((neighbor, c, d))
                    a = neighbor
                    break
        
        # Traverse from v to l
        a = v
        while a != l:
            for neighbor, c, d in adj[a]:
                if neighbor == up[0][a]:
                    path.append((neighbor, c, d))
                    a = neighbor
                    break
        
        # Now, for each edge in path, if its color is x, replace its length with y
        total = 0
        for neighbor, c, d in path:
            if c == x:
                total += y
            else:
                total += d
        
        print(total)