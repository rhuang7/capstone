import sys
import math
from collections import defaultdict, deque

def main():
    import sys
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
    tree = [[] for _ in range(N)]
    for i in range(N-1):
        u = i+1
        v = edges[i]
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)

    # Preprocess special nodes
    special_set = set(special)
    special_nodes = [i for i in range(N) if i+1 in special_set]

    # Precompute LCA and depths
    LOG = 15
    up = [[-1]*N for _ in range(LOG)]
    depth = [0]*N

    def dfs(u, p):
        up[0][u] = p
        for v in tree[u]:
            if v != p:
                depth[v] = depth[u]+1
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
            if depth[u] - (1<<k) >= depth[v]:
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

    # Precompute prefix sums for all paths from root to each node
    prefix = [{} for _ in range(N)]
    for i in range(N):
        prefix[i][0] = 0
        for j in range(1, N):
            prefix[i][j] = prefix[i][j-1] + cost[j]

    # For each query
    for _ in range(Q):
        s = int(data[idx])-1; idx +=1
        d = int(data[idx])-1; idx +=1
        W = int(data[idx]); idx +=1

        # Get all possible paths from s to d through special nodes
        min_x = float('inf')
        min_pv = float('inf')

        # For each special node
        for p in special_nodes:
            # Get path from s to p
            path_s_p = get_path(s, p)
            # Get path from p to d
            path_p_d = get_path(p, d)
            # Combine paths
            full_path = path_s_p + path_p_d[1:]

            # Compute prefix sums for full_path
            prefix_sum = [0]
            for i in range(len(full_path)):
                prefix_sum.append(prefix_sum[-1] + cost[full_path[i]])

            # Find best CTOT1 and CTOT2
            best_ctot1 = 0
            best_ctot2 = 0
            best_x = float('inf')
            best_pv = 0

            # Try all possible CTOT1 (sum from s to p)
            for i in range(len(prefix_sum)):
                ctot1 = prefix_sum[i]
                if ctot1 > W:
                    continue
                # Try all possible CTOT2 (sum from p to d)
                for j in range(i, len(prefix_sum)):
                    ctot2 = prefix_sum[j] - prefix_sum[i]
                    if ctot2 > W:
                        continue
                    x = abs(ctot1 - ctot2)
                    pv = ctot1 + ctot2
                    if x < best_x or (x == best_x and pv > best_pv):
                        best_x = x
                        best_pv = pv

            if best_x < min_x or (best_x == min_x and best_pv > min_pv):
                min_x = best_x
                min_pv = best_pv

        print(min_pv)

if __name__ == '__main__':
    main()