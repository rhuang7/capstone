import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0

    N = int(data[idx]); idx += 1
    NSP = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1

    edges = list(map(int, data[idx:idx + N - 1]))
    idx += N - 1

    costs = list(map(int, data[idx:idx + N]))
    idx += N

    special = list(map(int, data[idx:idx + NSP]))
    idx += NSP

    # Build tree
    tree = [[] for _ in range(N)]
    for i in range(N - 1):
        u = i + 1
        v = edges[i]
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    # Preprocess special nodes
    special_set = set(special)
    special_list = [i for i in range(N) if i in special_set]

    # Precompute all paths between every pair of nodes
    # For each query, we need to find the path between SNODE and DNODE
    # and then find the best PV for each special node on that path

    # Precompute LCA and path between nodes
    # Use binary lifting for LCA
    LOG = 15
    up = [[-1] * N for _ in range(LOG)]
    depth = [0] * N

    # BFS to compute depth and up[0]
    q = deque()
    q.append(0)
    up[0][0] = -1
    while q:
        u = q.popleft()
        for v in tree[u]:
            if up[0][v] == -1 and v != up[0][u]:
                up[0][v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    # Fill up table
    for k in range(1, LOG):
        for v in range(N):
            if up[k-1][v] != -1:
                up[k][v] = up[k-1][up[k-1][v]]

    # LCA function
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Bring u up to the depth of v
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

    # Function to get path between u and v
    def get_path(u, v):
        l = lca(u, v)
        path = []
        # Path from u to l
        while u != l:
            path.append(u)
            u = up[0][u]
        path.append(l)
        # Path from v to l (reverse)
        temp = []
        while v != l:
            temp.append(v)
            v = up[0][v]
        path += temp[::-1]
        return path

    # Precompute all paths for all pairs of nodes
    # But since N is 1000, it's too slow to precompute all paths
    # So we will compute the path for each query on the fly

    # For each query, we need to find the path between SNODE and DNODE
    # Then for each special node on that path, compute the best PV
    # Then choose the minimum x and maximum PV among all special nodes

    # For a given path, we need to find the best PV for each special node
    # For each special node P, we need to find the best CTOT1 and CTOT2
    # such that |CTOT1 - CTOT2| is minimized and PV is maximized

    # For a path, we can compute the prefix sums from SNODE to P and from P to DNODE
    # Then for each possible subset in the first part and second part, compute CTOT1 and CTOT2
    # and find the best pair

    # However, since the path can be up to 1000 nodes, and for each query, we need to process this, it's too slow
    # So we need to find a way to compute for each possible path the best PV for each special node

    # Let's proceed with the following approach:
    # For each query:
    # 1. Find the path between SNODE and DNODE
    # 2. For each special node P on the path:
    #    a. Compute the path from SNODE to P and from P to DNODE
    #    b. For each possible subset in the first part, compute CTOT1
    #    c. For each possible subset in the second part, compute CTOT2
    #    d. Find the pair (CTOT1, CTOT2) that minimizes |CTOT1 - CTOT2| and maximizes CTOT1 + CTOT2
    # 3. Among all special nodes, choose the one that gives the minimum x and maximum PV

    # But even this is too slow for N=1000 and Q=1000

    # So we need to find a way to precompute for each node the possible subsets of its path to other nodes
    # However, this is not feasible

    # Alternative approach:
    # For each query, find the path between SNODE and DNODE
    # For each special node P on the path:
    #   - Compute the path from SNODE to P
    #   - Compute the path from P to DNODE
    #   - For the first path, compute all possible CTOT1 values
    #   - For the second path, compute all possible CTOT2 values
    #   - Find the best pair (CTOT1, CTOT2) that minimizes |CTOT1 - CTOT2| and maximizes CTOT1 + CTOT2
    #   - Keep track of the best PV for this P
    #   - Finally, choose the best PV among all P

    # Now, for each path, we can compute the possible CTOT values using dynamic programming
    # For a path, the possible CTOT values can be computed by considering adding the current node's cost to previous subsets

    # So for a path, we can compute the possible CTOT values using a DP approach
    # For example, for a path of length m, we can compute all possible CTOT values up to W

    # Now, let's implement this

    for _ in range(Q):
        SNODE = int(data[idx]) - 1
        DNODE = int(data[idx+1]) - 1
        W = int(data[idx+2])
        idx += 3

        path = get_path(SNODE, DNODE)
        special_nodes_on_path = [p for p in special_list if p in path]

        best_pv = float('inf')
        for P in special_nodes_on_path:
            # Compute path from SNODE to P
            path1 = []
            u = SNODE
            while u != P:
                path1.append(u)
                u = up[0][u]
            path1.append(P)
            # Compute path from P to DNODE
            path2 = []
            u = DNODE
            while u != P:
                path2.append(u)
                u = up[0][u]
            path2 = path2[::-1]
            path2.append(P)

            # Compute all possible CTOT1 values for path1
            dp1 = [False] * (W + 1)
            dp1[0] = True
            for node in path1:
                cost = costs[node]
                for j in range(W, cost - 1, -1):
                    if dp1[j - cost]:
                        dp1[j] = True
            # Get all possible CTOT1 values
            ctot1 = [i for i in range(W + 1) if dp1[i]]

            # Compute all possible CTOT2 values for path2
            dp2 = [False] * (W + 1)
            dp2[0] = True
            for node in path2:
                cost = costs[node]
                for j in range(W, cost - 1, -1):
                    if dp2[j - cost]:
                        dp2[j] = True
            # Get all possible CTOT2 values
            ctot2 = [i for i in range(W + 1) if dp2[i]]

            # Find the best pair (ctot1, ctot2)
            min_x = float('inf')
            best_pv_pair = (0, 0)
            for c1 in ctot1:
                for c2 in ctot2:
                    x = abs(c1