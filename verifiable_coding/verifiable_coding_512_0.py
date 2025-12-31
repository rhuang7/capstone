import sys
import collections

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
    color_dict = collections.defaultdict(list)
    color_total = collections.defaultdict(int)
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
        color_total[c] += d

    # Build adjacency list
    adj = [[] for _ in range(N)]
    for a, b, c, d in edges:
        adj[a].append((b, c, d))
        adj[b].append((a, c, d))

    # Precompute LCA and depth for each node
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

    def get_dist(u, v):
        ancestor = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[ancestor]

    # Precompute for each color the total length
    color_total = collections.defaultdict(int)
    for a, b, c, d in edges:
        color_total[c] += d

    # For each query, compute the distance
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

        # Compute the distance with the given color change
        total = 0
        for a, b, c, d in edges:
            if c == x:
                total += y
            else:
                total += d

        output.append(str(total))

    print('\n'.join(output))