import sys
import math
from collections import defaultdict, deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    edges = []
    color_dict = defaultdict(list)
    color_sum = defaultdict(int)
    color_count = defaultdict(int)

    for _ in range(N-1):
        a = int(data[idx]) - 1
        idx += 1
        b = int(data[idx]) - 1
        idx += 1
        c = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        edges.append((a, b, c, d))
        color_dict[c].append((a, b, d))
        color_sum[c] += d
        color_count[c] += 1

    # Preprocess for LCA
    LOG = 20
    parent = [[-1]*N for _ in range(LOG)]
    depth = [0]*N

    # Build tree
    tree = [[] for _ in range(N)]
    for a, b, c, d in edges:
        tree[a].append((b, c, d))
        tree[b].append((a, c, d))

    # BFS to set depth and parent[0]
    q = deque()
    q.append(0)
    parent[0][0] = -1
    while q:
        u = q.popleft()
        for v, c, d in tree[u]:
            if parent[0][v] == -1 and v != parent[0][u]:
                parent[0][v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    # Build binary lifting table
    for k in range(1, LOG):
        for v in range(N):
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

    # Function to get distance between u and v
    def get_dist(u, v):
        ancestor = lca(u, v)
        dist = 0
        for k in range(LOG-1, -1, -1):
            if parent[k][u] != -1 and parent[k][u] != ancestor:
                dist += color_sum.get(parent[k][u], 0)
                u = parent[k][u]
        for k in range(LOG-1, -1, -1):
            if parent[k][v] != -1 and parent[k][v] != ancestor:
                dist += color_sum.get(parent[k][v], 0)
                v = parent[k][v]
        return dist

    # Process queries
    output = []
    for _ in range(Q):
        x = int(data[idx]) - 1
        idx += 1
        y = int(data[idx])
        idx += 1
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1

        # Temporarily update color_sum and color_count
        temp_sum = color_sum.copy()
        temp_count = color_count.copy()
        if x in temp_sum:
            temp_sum[x] = y * temp_count[x]
        else:
            temp_sum[x] = 0

        # Compute distance
        dist = get_dist(u, v)
        output.append(str(dist))

    print('\n'.join(output))