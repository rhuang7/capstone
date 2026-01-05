import sys
import math
from collections import deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx]); idx +=1
    NSP = int(data[idx]); idx +=1
    Q = int(data[idx]); idx +=1
    
    edges = list(map(int, data[idx:idx+N-1]))
    idx += N-1
    
    cost = list(map(int, data[idx:idx+N]))
    idx += N
    
    special = list(map(int, data[idx:idx+NSP]))
    idx += NSP
    
    queries = []
    for _ in range(Q):
        s = int(data[idx]); idx +=1
        d = int(data[idx]); idx +=1
        w = int(data[idx]); idx +=1
        queries.append((s, d, w))
    
    # Build tree
    tree = [[] for _ in range(N+1)]
    for i in range(N-1):
        u = i+1
        v = edges[i]
        tree[u].append(v)
        tree[v].append(u)
    
    # Preprocess special nodes
    special_set = set(special)
    
    # Precompute LCA and depth
    LOG = 20
    up = [[-1]*(N+1) for _ in range(LOG)]
    depth = [0]*(N+1)
    
    def dfs(u, p):
        up[0][u] = p
        for v in tree[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    dfs(1, -1)
    
    for k in range(1, LOG):
        for v in range(1, N+1):
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
    
    # Precompute path from u to v
    def get_path(u, v):
        l = lca(u, v)
        path = []
        while u != l:
            path.append(u)
            u = up[0][u]
        path.append(l)
        while v != l:
            path.append(v)
            v = up[0][v]
        return path
    
    # Precompute prefix sums for each special node
    # For each special node, precompute all possible prefix sums along the path from root to it
    # And also the path from root to it
    special_prefix = []
    special_paths = []
    for node in special:
        path = []
        u = node
        while u != -1:
            path.append(u)
            u = up[0][u]
        special_paths.append(path)
        prefix = [0]
        current_sum = 0
        for u in path:
            current_sum += cost[u-1]
            prefix.append(current_sum)
        special_prefix.append(prefix)
    
    # For each query, find the path between s and d, and for each special node on the path, compute the best PV
    # The best PV is the minimum x, and then maximum PV
    # So for each query, we need to find the best PV for all special nodes on the path between s and d
    # But since the path is from s to d, and the pivot can be any special node on that path, we need to check all special nodes on the path between s and d
    
    # For each query, find the path between s and d
    def get_path_between(s, d):
        l = lca(s, d)
        path = []
        while s != l:
            path.append(s)
            s = up[0][s]
        path.append(l)
        while d != l:
            path.append(d)
            d = up[0][d]
        return path
    
    # For a given path, find all special nodes on it
    def get_special_nodes_on_path(path):
        return [node for node in path if node in special_set]
    
    # For a given path, find all possible subsets of nodes on the path from s to p and p to d
    # For each special node p on the path, compute the best PV
    # For each p, we need to find the best CTOT1 and CTOT2 such that |CTOT1 - CTOT2| is minimized and PV is maximized
    # To do this, we can use dynamic programming for each segment of the path
    # For the path from s to p, we can compute all possible subset sums up to W
    # Similarly for the path from p to d
    # Then, for each possible CTOT1 and CTOT2, we can compute the absolute difference and find the best pair
    
    # Precompute for all possible paths
    # But since the number of queries is 1000 and the number of special nodes is 10, this might be feasible
    
    # For each query, process as follows:
    for s, d, w in queries:
        path = get_path_between(s, d)
        special_nodes = get_special_nodes_on_path(path)
        if not special_nodes:
            # No special nodes on the path, so the pivot must be one of the nodes on the path
            # But according to the problem statement, the pivot must be a special node
            # So in this case, the answer is undefined, but according to the problem statement, there is always a solution
            # So this case is not possible
            pass
        best_pv = float('inf')
        for p in special_nodes:
            # Get the path from s to p
            path_s_p = []
            u = s
            while u != p:
                path_s_p.append(u)
                u = up[0][u]
            path_s_p.append(p)
            # Get the path from p to d
            path_p_d = []
            u = d
            while u != p:
                path_p_d.append(u)
                u = up[0][u]
            path_p_d.append(p)
            # Now, for the path from s to p, compute all possible subset sums up to W
            # Similarly for the path from p to d
            # Then, for each possible CTOT1 and CTOT2, compute |CTOT1 - CTOT2| and find the minimum
            # And then find the maximum PV for that minimum
            # To do this, we can use dynamic programming for each segment
            # For the path from s to p
            # We can compute all possible subset sums up to W
            # Similarly for the path from p to d
            # Then, for each possible CTOT1 and CTOT2, compute |CTOT1 - CTOT2|
            # We need to find the pair (CTOT1, CTOT2) that minimizes |CTOT1 - CTOT2|, and among those, maximizes CTOT1 + CTOT2
            # So for each segment, we can compute all possible subset sums up to W
            # For the path from s to p, we can compute all possible subset sums
            # For the path from p to d, we can compute all possible subset sums
            # Then, for all possible CTOT1 and CTOT2, we can compute the absolute difference and find the best pair
            
            # Compute possible subset sums for path_s_p
            # We can use a dynamic programming approach
            # Initialize a set of possible sums
            # For each node in the path, we can add its cost to the existing sums
            # We can do this for the path_s_p
            # Similarly for path_p_d
            # But since the path can be up to 1000 nodes, and W is up to 1000, this might be feasible
            
            # Compute possible subset sums for path_s_p
            # We can use a set of possible sums
            # Start with 0
            # For each node in the path, we can add its cost to the existing sums
            # But we need to keep track of the maximum possible sum up to W
            # So we can use a set of possible sums for each node in the path
            # For the path_s_p
            dp_s_p = [set() for _ in range(len(path_s_p))]
            dp_s_p[0].add(0)
            for i in range(len(path_s_p)):
                for s in dp_s_p[i]:
                    dp_s_p[i+1].add(s)
                    dp_s_p[i+1].add(s + cost[path_s_p[i]-1])
            # Now, for the path_s_p, the possible