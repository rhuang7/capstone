import sys
import math
from collections import deque, defaultdict

input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        adj = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        # Precompute depth and parent for LCA
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
            for v in adj[u]:
                if parent[0][v] == -1 and v != 1:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        # Fill parent table
        for k in range(1, LOG):
            for v in range(1, N + 1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Bring u up to the depth of v
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
        # Function to get distance between two nodes
        def dist(u, v):
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
            if da + db < dist(a, b):
                results.append(-1)
                continue
            # Find possible candidates
            # Case 1: x is on the path from a to b
            # Case 2: x is on the path from a to lca(a,b)
            # Case 3: x is on the path from b to lca(a,b)
            l = lca(a, b)
            # Check if a is on the path from l to b
            if parent[0][a] == l:
                # x is on the path from a to l
                # distance from x to a is da
                # distance from x to b is db
                # x is at distance da from a, which is on the path from a to l
                # so x is at depth depth[a] - da
                if depth[a] - da < depth[l]:
                    results.append(-1)
                    continue
                x = a
                for k in range(LOG-1, -1, -1):
                    if depth[x] - (1 << k) >= depth[l] - da:
                        x = parent[k][x]
                if dist(x, a) == da and dist(x, b) == db:
                    results.append(x)
                else:
                    results.append(-1)
            else:
                # Check if b is on the path from l to a
                if parent[0][b] == l:
                    # x is on the path from b to l
                    # distance from x to b is db
                    # distance from x to a is da
                    # x is at depth depth[b] - db
                    if depth[b] - db < depth[l]:
                        results.append(-1)
                        continue
                    x = b
                    for k in range(LOG-1, -1, -1):
                        if depth[x] - (1 << k) >= depth[l] - db:
                            x = parent[k][x]
                    if dist(x, a) == da and dist(x, b) == db:
                        results.append(x)
                    else:
                        results.append(-1)
                else:
                    # x is on the path from l to a
                    # distance from x to a is da
                    # distance from x to b is db
                    # x is at depth depth[l] + da
                    if depth[l] + da > depth[a]:
                        results.append(-1)
                        continue
                    x = l
                    for k in range(LOG-1, -1, -1):
                        if depth[x] + (1 << k) <= depth[l] + da:
                            x = parent[k][x]
                    if dist(x, a) == da and dist(x, b) == db:
                        results.append(x)
                    else:
                        results.append(-1)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')