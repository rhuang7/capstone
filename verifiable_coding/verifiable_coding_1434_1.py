import sys
import math
from collections import defaultdict, deque

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

    # Build tree
    tree = defaultdict(list)
    for i in range(N-1):
        u = i+1
        v = edges[i]
        tree[u].append(v)
        tree[v].append(u)

    # Preprocess special nodes
    special_set = set(special)
    special_nodes = [i for i in range(1, N+1) if i in special_set]

    # Preprocess LCA and depth
    LOG = 20
    up = [[-1]* (N+1) for _ in range(LOG)]
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

    # Preprocess path from u to v
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

    # Preprocess prefix sums for each path from root
    # We'll use a dictionary to store prefix sums for each node
    # For each node, we'll store a list of prefix sums for the path from root to it
    # But since the tree is undirected, we need to process it with parent tracking

    # Preprocess prefix sums for each node
    prefix_sums = [{} for _ in range(N+1)]
    def dfs_prefix(u, parent):
        # Store the path from root to u
        path = []
        while u != -1:
            path.append(u)
            u = parent[u]
        path = path[::-1]
        # Compute prefix sums
        ps = [0]
        for node in path:
            ps.append(ps[-1] + cost[node-1])
        # Store in prefix_sums for this node
        prefix_sums[node] = ps
        for v in tree[node]:
            if v != parent[node]:
                parent[v] = node
                dfs_prefix(v, parent)

    parent = [-1]*(N+1)
    dfs_prefix(1, parent)

    # For each query, find the path from s to d, then for each special node p on the path,
    # compute the best CTOT1 and CTOT2 for the path s->p and p->d
    # Then find the minimum x and corresponding PV

    def solve():
        for _ in range(Q):
            s = int(data[idx]); idx +=1
            d = int(data[idx]); idx +=1
            W = int(data[idx]); idx +=1

            # Get the path from s to d
            path = get_path(s, d)
            # For each special node p in the path
            min_x = float('inf')
            min_pv = float('inf')

            for p in special_nodes:
                if p not in path:
                    continue
                # Get the path from s to p
                path1 = get_path(s, p)
                # Get the path from p to d
                path2 = get_path(p, d)
                # Combine the paths
                full_path = path1 + path2[1:]

                # Compute prefix sums for path1 and path2
                ps1 = prefix_sums[path1[-1]]
                ps2 = prefix_sums[path2[-1]]

                # Find best CTOT1 for path1
                best1 = 0
                best1_val = 0
                for i in range(len(ps1)):
                    if ps1[i] <= W:
                        best1_val = max(best1_val, ps1[i])
                        best1 = i
                    else:
                        break
                # Find best CTOT2 for path2
                best2 = 0
                best2_val = 0
                for i in range(len(ps2)):
                    if ps2[i] <= W:
                        best2_val = max(best2_val, ps2[i])
                        best2 = i
                    else:
                        break

                # Compute PV
                pv = best1_val + best2_val
                x = abs(best1_val - best2_val)

                if x < min_x or (x == min_x and pv > min_pv):
                    min_x = x
                    min_pv = pv

            print(min_pv)

    solve()

if __name__ == '__main__':
    main()