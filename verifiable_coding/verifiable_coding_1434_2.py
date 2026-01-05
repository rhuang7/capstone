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

    # Preprocess prefix sums for all paths from root
    # For each node, store prefix sums for all possible paths from root to it
    # But since the tree is big, we need to find a way to compute path sums on the fly
    # For each query, we need to find the path from SNODE to DNODE, then for each special node P on that path, compute the best CTOT1 and CTOT2

    def get_path_sum(u, v):
        path = get_path(u, v)
        total = 0
        path_sum = []
        for node in path:
            total += cost[node-1]
            path_sum.append(total)
        return path_sum

    def solve():
        for _ in range(Q):
            s = int(data[idx]); idx +=1
            d = int(data[idx]); idx +=1
            W = int(data[idx]); idx +=1

            path = get_path(s, d)
            path_sum = get_path_sum(s, d)
            total_sum = path_sum[-1]

            min_x = float('inf')
            best_pv = 0

            for p in special_nodes:
                if p not in path:
                    continue

                # Find index of p in path
                p_idx = path.index(p)

                # Get prefix sums from s to p
                prefix1 = path_sum[:p_idx+1]
                # Get prefix sums from p to d
                prefix2 = path_sum[p_idx:]

                # Find best CTOT1 and CTOT2 for prefix1 and prefix2
                # For prefix1, find the best CTOT1 <= W
                # For prefix2, find the best CTOT2 <= W

                # For prefix1
                best1 = 0
                best1_val = 0
                for val in prefix1:
                    if val <= W:
                        best1_val = max(best1_val, val)
                        best1 = val
                    else:
                        break
                # Try to find a subset with sum <= W that gives max CTOT1
                # We can use a knapsack-like approach for prefix1
                # But since W is small, we can do it with a DP

                # For prefix1
                dp1 = [0]*(W+1)
                for val in prefix1:
                    for w in range(W, val-1, -1):
                        dp1[w] = max(dp1[w], dp1[w - val] + val)
                best1 = max(dp1)

                # For prefix2
                dp2 = [0]*(W+1)
                for val in prefix2:
                    for w in range(W, val-1, -1):
                        dp2[w] = max(dp2[w], dp2[w - val] + val)
                best2 = max(dp2)

                # Now, find the best CTOT1 and CTOT2 that minimize |CTOT1 - CTOT2|
                # We can try all possible CTOT1 and CTOT2 that are <= W
                # But since W is small, we can do this with two loops

                min_diff = float('inf')
                best_pv_val = 0

                for c1 in range(0, W+1):
                    if c1 > best1:
                        continue
                    for c2 in range(0, W+1):
                        if c2 > best2:
                            continue
                        diff = abs(c1 - c2)
                        if diff < min_diff:
                            min_diff = diff
                            best_pv_val = c1 + c2
                        elif diff == min_diff:
                            if c1 + c2 > best_pv_val:
                                best_pv_val = c1 + c2

                if min_diff < min_x:
                    min_x = min_diff
                    best_pv = best_pv_val
                elif min_diff == min_x:
                    if best_pv_val > best_pv:
                        best_pv = best_pv_val

            print(best_pv)

    solve()

if __name__ == '__main__':
    main()