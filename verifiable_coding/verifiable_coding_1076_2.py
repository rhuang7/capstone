import sys
import math
from collections import deque, defaultdict

def main():
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
        
        # Build the tree
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Precompute depths and parents for LCA
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
        
        # Function to get the k-th ancestor
        def get_kth_ancestor(u, k):
            for i in range(LOG):
                if k & (1 << i):
                    u = parent[i][u]
                    if u == -1:
                        return -1
            return u
        
        # Function to get the distance between two nodes
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
            if da + db < distance(a, b) or da + db > distance(a, b) + 2 * (depth[a] + depth[b] - 2 * depth[lca(a, b)]):
                results.append(-1)
                continue
            
            # Find the path from a to b
            l = lca(a, b)
            path = []
            u = a
            while u != l:
                path.append(u)
                u = parent[0][u]
            path.append(l)
            u = b
            while u != l:
                path.append(u)
                u = parent[0][u]
            path.reverse()
            
            # Find all nodes on the path
            nodes_on_path = set(path)
            
            # Check for possible candidates
            candidates = []
            for node in nodes_on_path:
                if distance(node, a) == da and distance(node, b) == db:
                    candidates.append(node)
            
            if not candidates:
                results.append(-1)
            else:
                results.append(candidates[0])
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()