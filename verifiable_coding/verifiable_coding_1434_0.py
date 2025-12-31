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
    for i in range(1, N):
        u = i+1
        v = edges[i-1]
        tree[u].append(v)
        tree[v].append(u)

    # Preprocess special nodes
    special_set = set(special)

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
    # But since the tree is arbitrary, we need to process paths dynamically

    # Function to get path from u to v
    def get_path_nodes(u, v):
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

    # Function to compute all possible subset sums for a path
    def get_subset_sums(path, max_w):
        n = len(path)
        dp = [set() for _ in range(n+1)]
        dp[0].add(0)
        for i in range(n):
            for s in dp[i]:
                dp[i+1].add(s)
                dp[i+1].add(s + cost[path[i]])
        # Filter sums <= max_w
        res = [s for s in dp[n] if s <= max_w]
        return res

    # Function to find best CTOT1 and CTOT2 for a given path and W
    def find_best(path, W):
        # Get all possible subset sums for path
        sums = get_subset_sums(path, W)
        # For each possible CTOT1, find best CTOT2
        best_x = float('inf')
        best_pv = 0
        for ctot1 in sums:
            # Find best ctot2 such that |ctot1 - ctot2| is minimized
            # And ctot2 is in sums
            best_ctot2 = None
            best_diff = float('inf')
            for ctot2 in sums:
                diff = abs(ctot1 - ctot2)
                if diff < best_diff:
                    best_diff = diff
                    best_ctot2 = ctot2
                elif diff == best_diff:
                    if ctot2 > best_ctot2:
                        best_ctot2 = ctot2
            # Compute PV = ctot1 + ctot2
            pv = ctot1 + best_ctot2
            if best_diff < best_x or (best_diff == best_x and pv > best_pv):
                best_x = best_diff
                best_pv = pv
        return best_pv

    # Solve each query
    for s, d, w in queries:
        # Get path from s to d
        path = get_path_nodes(s, d)
        # For each special node on the path, compute PV
        min_pv = float('inf')
        for p in special_set:
            if p in path:
                # Split path into two parts: s to p and p to d
                part1 = path[:path.index(p)+1]
                part2 = path[path.index(p):]
                # Compute best CTOT1 and CTOT2 for part1 and part2
                # CTOT1 is subset of part1, CTOT2 is subset of part2
                # Find best CTOT1 and CTOT2 for part1 and part2
                sums1 = get_subset_sums(part1, w)
                sums2 = get_subset_sums(part2, w)
                # Find best CTOT1 and CTOT2
                best_x = float('inf')
                best_pv = 0
                for ctot1 in sums1:
                    for ctot2 in sums2:
                        diff = abs(ctot1 - ctot2)
                        if diff < best_x or (diff == best_x and (ctot1 + ctot2) > best_pv):
                            best_x = diff
                            best_pv = ctot1 + ctot2
                if best_pv < min_pv:
                    min_pv = best_pv
        print(min_pv)

if __name__ == '__main__':
    main()