import sys
import collections

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
    color_map = collections.defaultdict(list)
    color_dict = {}
    total_color_count = 0
    
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
        if c not in color_dict:
            color_dict[c] = 0
        color_dict[c] += 1
        total_color_count += 1
    
    # Preprocess for LCA
    LOG = 20
    up = [[-1]*N for _ in range(LOG)]
    depth = [0]*N
    parent = [0]*N
    
    def dfs(u, p):
        parent[u] = p
        for v, _, _ in edges:
            if v == u:
                dfs(v, u)
    
    dfs(0, -1)
    
    for i in range(1, N):
        up[0][i] = parent[i]
    
    for k in range(1, LOG):
        for i in range(N):
            if up[k-1][i] != -1:
                up[k][i] = up[k-1][up[k-1][i]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for k in range(LOG-1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return parent[u]
    
    def get_distance(u, v):
        l = lca(u, v)
        dist = 0
        for i in range(N):
            if i == l:
                continue
            if (parent[i] == l or parent[l] == i):
                dist += 1
        return dist
    
    for _ in range(Q):
        x = int(data[idx]) - 1
        idx += 1
        y = int(data[idx])
        idx += 1
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        
        # For each query, we need to calculate the distance between u and v with the color x's edge lengths changed to y
        # We'll do this by modifying the edge lengths temporarily and then calculating the distance
        # But since we can't modify the original data, we'll create a copy of the edge lengths and modify it
        
        # Create a copy of the edge lengths
        edge_lengths = [0] * (N-1)
        for i in range(N-1):
            edge_lengths[i] = edges[i][3]
        
        # Modify the edge lengths for color x
        for a, b, c, d in edges:
            if c == x:
                edge_lengths[edges.index((a, b, c, d))] = y
        
        # Now calculate the distance between u and v using the modified edge lengths
        # We'll do this by performing a BFS or DFS to find the path and sum the edge lengths
        
        # BFS to find the path
        visited = [False] * N
        prev = [-1] * N
        queue = [u]
        visited[u] = True
        while queue:
            current = queue.pop(0)
            if current == v:
                break
            for i in range(N-1):
                a, b, c, d = edges[i]
                if (a == current and b == parent[current] and c == x) or (b == current and a == parent[current] and c == x):
                    if not visited[b]:
                        visited[b] = True
                        prev[b] = current
                        queue.append(b)
                if (a == current and b == parent[current] and c != x) or (b == current and a == parent[current] and c != x):
                    if not visited[b]:
                        visited[b] = True
                        prev[b] = current
                        queue.append(b)
        
        # Reconstruct the path
        path = []
        current = v
        while current != u:
            path.append(current)
            current = prev[current]
        path.append(u)
        path.reverse()
        
        # Calculate the distance
        dist = 0
        for i in range(len(path)-1):
            a = path[i]
            b = path[i+1]
            for edge in edges:
                if (edge[0] == a and edge[1] == b) or (edge[0] == b and edge[1] == a):
                    if edge[2] == x:
                        dist += y
                    else:
                        dist += edge[3]
                    break
        
        print(dist)