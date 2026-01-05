import sys
import math
from collections import deque, defaultdict

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
        up = [[-1]*(N+1) for _ in range(LOG)]
        depth = [0]*(N+1)
        
        # BFS to compute depth and up[0]
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
        
        # Preprocess up table
        for k in range(1, LOG):
            for v in range(1, N+1):
                if up[k-1][v] != -1:
                    up[k][v] = up[k-1][up[k-1][v]]
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u to the same depth as v
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
        
        # Function to find the k-th ancestor of a node
        def get_kth_ancestor(u, k):
            for i in range(LOG):
                if k & (1 << i):
                    u = up[i][u]
                    if u == -1:
                        return -1
            return u
        
        # Function to find the distance between two nodes
        def distance(u, v):
            ancestor = lca(u, v)
            return depth[u] + depth[v] - 2 * depth[ancestor]
        
        # Precompute all distances from each node
        # This is not feasible for large N, so we'll compute on the fly
        # For each query, we'll find possible candidates
        
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
                results.append(-1)
                continue
            
            # Find possible nodes x such that d(x,a) = da and d(x,b) = db
            # The set of such nodes is the intersection of two sets:
            # 1. Nodes at distance da from a
            # 2. Nodes at distance db from b
            
            # Find all nodes at distance da from a
            # This is done by BFS
            def get_nodes_at_dist(start, dist):
                visited = [False]*(N+1)
                q = deque()
                q.append((start, 0))
                visited[start] = True
                res = []
                while q:
                    u, d = q.popleft()
                    if d == dist:
                        res.append(u)
                    elif d < dist:
                        for v in adj[u]:
                            if not visited[v]:
                                visited[v] = True
                                q.append((v, d+1))
                return res
            
            nodes_a = get_nodes_at_dist(a, da)
            nodes_b = get_nodes_at_dist(b, db)
            
            # Find intersection
            res = []
            for x in nodes_a:
                if x in nodes_b:
                    res.append(x)
            
            if not res:
                results.append(-1)
            else:
                results.append(res[0])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()