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

    costs = list(map(int, data[idx:idx+N]))
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
    special_nodes = [i for i in range(1, N+1) if i in special_set]

    # Preprocess LCA and depth
    LOG = 17
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

    # Preprocess prefix sums for all possible paths
    # For each special node, precompute prefix sums from root to it
    # And also from it to root
    # But since the tree is undirected, we can do BFS from each special node
    # And for each node, store the path from the special node to it
    # But this would be too slow for N=1000 and NSP=10

    # Instead, for each query, we can find the path between s and d, then for each special node on the path, compute the best PV

    # But for each query, the path between s and d is unique, and we can find it
    # Then for each special node on the path, compute the best PV

    # So for each query, we do the following:
    # 1. Find the path between s and d
    # 2. For each special node on the path, compute the best PV
    # 3. Take the minimum x, and if multiple, take the maximum PV

    # But for each query, the path can be up to O(N) in length, and for each special node on the path, we need to process the path from s to p and p to d

    # So for each query, we can:
    # 1. Find the path between s and d
    # 2. For each special node p in the path, compute the best PV for that p
    # 3. Take the minimum x and corresponding PV

    # But for each query, the path can be up to O(N) in length, and for each special node, we need to process O(N) steps

    # So the total time is O(Q * N * NSP), which for N=1000, Q=1000, NSP=10, is 10^7 operations, which is acceptable

    # So we proceed with this approach

    for s, d, w in queries:
        path = get_path(s, d)
        min_x = float('inf')
        best_pv = 0

        for p in special_nodes:
            if p not in path:
                continue

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
            path_p_d.reverse()

            # Now, for path_s_p and path_p_d, compute the best CTOT1 and CTOT2

            # For path_s_p, find the best CTOT1 (sum of subset with sum <= W)
            # Similarly for path_p_d

            # We can use dynamic programming for each path

            # For path_s_p
            # dp[i][j] = whether it is possible to get sum j using first i nodes
            # But since W is up to 1000, and the path can be up to 1000 nodes, the total sum could be up to 1000*1000 = 1e6, which is too big

            # So we need a better approach

            # Instead, for each path, we can find the best CTOT1 and CTOT2

            # For path_s_p, we can find the best CTOT1 (sum <= W) and the best CTOT2 (sum <= W) for the path_p_d

            # For each path, we can compute all possible subset sums, and then for each possible CTOT1, find the best CTOT2 that minimizes |CTOT1 - CTOT2|

            # But for each path, the maximum sum is up to 1000*1000 = 1e6, which is too big

            # So we need a better way

            # Let's think: for each path, we can find the best CTOT1 and CTOT2 that minimize |CTOT1 - CTOT2|, and maximize PV = CTOT1 + CTOT2

            # For the path from s to p, we can compute all possible subset sums (CTOT1) that are <= W

            # Similarly for the path from p to d, compute all possible subset sums (CTOT2) that are <= W

            # Then, for each CTOT1 in the first set, and CTOT2 in the second set, compute |CTOT1 - CTOT2|, and find the minimum, and among those, the maximum PV

            # But this is O(M * K), where M is the number of CTOT1 and K is the number of CTOT2, which could be up to 1e3 * 1e3 = 1e6 per query, which is acceptable

            # So for each path, we can compute all possible subset sums that are <= W, and store them in a set

            # For the path_s_p, compute all possible subset sums (CTOT1) that are <= W
            # For the path_p_d, compute all possible subset sums (CTOT2) that are <= W

            # Then, for each CTOT1 in the first set, find the CTOT2 in the second set that minimizes |CTOT1 - CTOT2|, and among those, choose the one that maximizes CTOT1 + CTOT2

            # Let's implement this

            # Compute subset sums for path_s_p
            def get_subset_sums(path, max_w):
                n = len(path)
                dp = [False] * (max_w + 1)
                dp[0] = True
                for i in range(n):
                    val = costs[path[i]-1]
                    for j in range(max_w, val-1, -1):
                        if dp[j - val]:
                            dp[j] = True
                subset_sums = [i for i in range(max_w+1) if dp[i]]
                return subset_sums

            # Compute subset sums for path_s_p