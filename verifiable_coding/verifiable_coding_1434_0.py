import sys
import math
from collections import deque, defaultdict

sys.setrecursionlimit(1 << 25)

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

    queries = []
    for _ in range(Q):
        s = int(data[idx]); idx +=1
        d = int(data[idx]); idx +=1
        w = int(data[idx]); idx +=1
        queries.append( (s, d, w) )

    # Build tree
    tree = [[] for _ in range(N+1)]
    for i in range(1, N):
        v = edges[i-1]
        tree[i].append(v)
        tree[v].append(i)

    # Preprocess special nodes
    special_set = set(special)

    # Precompute LCA and depths
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

    # Precompute paths between nodes
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

    # Precompute prefix sums for all possible paths
    # But since N is up to 1000, and queries are up to 1000, it's not feasible to precompute all paths
    # So for each query, we compute the path and then process it

    # For each query, find the path between s and d, then for each special node on the path, compute the best CTOT1 and CTOT2

    def solve_query(s, d, w):
        path = get_path(s, d)
        # Find all special nodes on the path
        special_on_path = [x for x in path if x in special_set]
        if not special_on_path:
            return 0  # No special nodes, so pivot can't be chosen, but the problem says it's valid
        # For each special node on the path, compute the best CTOT1 and CTOT2
        min_x = float('inf')
        best_pv = 0
        for p in special_on_path:
            # Get path from s to p
            path1 = get_path(s, p)
            # Get path from p to d
            path2 = get_path(p, d)
            # Combine the two paths
            full_path = path1 + path2[1:]
            # Compute prefix sums for full_path
            prefix = [0]*(len(full_path)+1)
            for i in range(len(full_path)):
                prefix[i+1] = prefix[i] + cost[full_path[i]-1]
            # Now find best CTOT1 and CTOT2
            # CTOT1 is sum of subset in path1 (s to p)
            # CTOT2 is sum of subset in path2 (p to d)
            # We need to find CTOT1 and CTOT2 such that |CTOT1 - CTOT2| is minimized, and PV is maximized
            # For path1, we can find all possible CTOT1 values
            # For path2, we can find all possible CTOT2 values
            # Then for all pairs (ct1, ct2), compute |ct1 - ct2| and choose the best
            # But since W is up to 1000, and the path can be up to 2000 nodes, we need an efficient way
            # So we can use dynamic programming for each path
            # For path1: find all possible CTOT1 values up to W
            # For path2: find all possible CTOT2 values up to W
            # Then for all possible ct1 and ct2, compute |ct1 - ct2| and find the minimum
            # Also, for the minimum |ct1 - ct2|, we need to maximize ct1 + ct2
            # So we can precompute for path1 and path2 the best possible ct1 and ct2 for each possible difference

            # Compute possible CTOT1 values for path1
            dp1 = [False]*(W+1)
            dp1[0] = True
            for node in path1:
                val = cost[node-1]
                for j in range(W, val-1, -1):
                    if dp1[j - val]:
                        dp1[j] = True
            # Compute possible CTOT2 values for path2
            dp2 = [False]*(W+1)
            dp2[0] = True
            for node in path2:
                val = cost[node-1]
                for j in range(W, val-1, -1):
                    if dp2[j - val]:
                        dp2[j] = True
            # Now find the best pair (ct1, ct2)
            best_diff = float('inf')
            best_pv_val = 0
            for ct1 in range(W+1):
                if not dp1[ct1]:
                    continue
                for ct2 in range(W+1):
                    if not dp2[ct2]:
                        continue
                    diff = abs(ct1 - ct2)
                    if diff < best_diff or (diff == best_diff and (ct1 + ct2) > best_pv_val):
                        best_diff = diff
                        best_pv_val = ct1 + ct2
            # Now, for the best_diff, find the maximum possible ct1 + ct2
            # But we need to find the actual ct1 and ct2 that achieve this
            # So we need to find the best ct1 and ct2 that give the best_diff and max ct1 + ct2
            # So we need to iterate through all possible ct1 and ct2 again
            best_pv_val = 0
            best_ct1 = 0
            best_ct2 = 0
            for ct1 in range(W+1):
                if not dp1[ct1]:
                    continue
                for ct2 in range(W+1):
                    if not dp2[ct2]:
                        continue
                    diff = abs(ct1 - ct2)
                    if diff < best_diff or (diff == best_diff and (ct1 + ct2) > best_pv_val):
                        best_diff = diff
                        best_pv_val = ct1 + ct2
                        best_ct1 = ct1
                        best_ct2 = ct2
            # Now, the best_pv is best_pv_val
            # But we need to check if there are multiple pairs with the same best_diff and best_pv_val
            # However, since we are choosing the maximum PV, this is already handled
            # So update the global min_x and best_pv
            if best_diff < min_x or (best_diff == min_x and best_pv_val > best_pv):
                min_x = best_diff
                best_pv = best_pv_val
        return best_pv

    for s, d, w in queries:
        res = solve_query(s, d, w)
        print(res)

if __name__ == '__main__':
    main()