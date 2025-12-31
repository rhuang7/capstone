import sys
import sys
sys.setrecursionlimit(1 << 25)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    edges = [[] for _ in range(N + 1)]
    idx = 1
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        edges[u].append(v)
        edges[v].append(u)
        idx += 2

    from collections import deque

    # Compute depth and parent for each node
    depth = [0] * (N + 1)
    parent = [0] * (N + 1)
    visited = [False] * (N + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v in edges[u]:
            if not visited[v] and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                visited[v] = True
                q.append(v)

    # Count the number of leaves (nodes with degree 1 and not root)
    leaves = 0
    for i in range(1, N + 1):
        if len(edges[i]) == 1 and i != 1:
            leaves += 1

    # The maximum number of connected components is the number of leaves
    print(leaves)

if __name__ == '__main__':
    solve()