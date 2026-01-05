import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    edges = []
    color_map = defaultdict(list)
    color_dict = defaultdict(int)
    total_color = 0

    for _ in range(N - 1):
        a = int(data[idx]) - 1
        idx += 1
        b = int(data[idx]) - 1
        idx += 1
        c = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        edges.append((a, b, c, d))
        color_map[c].append((a, b, d))
        color_dict[c] = d
        total_color = max(total_color, c)

    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Build adjacency list
    adj = [[] for _ in range(N)]
    for a, b, c, d in edges:
        adj[a].append((b, c, d))
        adj[b].append((a, c, d))

    # Preprocess LCA
    LOG = 20
    up = [[-1] * N for _ in range(LOG)]
    depth = [0] * N

    def dfs(u, p):
        up[0][u] = p
        for v, c, d in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
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
            if depth[u] - (1 << k) >= depth[v]:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if up[k][u] != -1 and up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    def distance(u, v):
        l = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[l]

    # Preprocess color to distance
    color_to_dist = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_to_dist[c] = total

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)
    for c in color_map:
        total = 0
        for a, b, d in color_map[c]:
            total += d
        color_total[c] = total

    # Preprocess color to individual distances
    color_dist = defaultdict(list)
    for c in color_map:
        for a, b, d in color_map[c]:
            color_dist[c].append(d)

    # Preprocess color to count
    color_count = defaultdict(int)
    for c in color_map:
        color_count[c] = len(color_map[c])

    # Preprocess color to total distance
    color_total = defaultdict(int)