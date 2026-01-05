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

    # Compute the depth of each node
    depth = [0] * (N + 1)
    visited = [False] * (N + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v in edges[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                q.append(v)

    # Count the number of leaves at each depth
    leaf_count = [0] * (N + 1)
    for i in range(1, N + 1):
        if len(edges[i]) == 1:
            leaf_count[depth[i]] += 1

    # The maximum number of components is the number of leaves at the deepest level
    max_depth = max(depth)
    print(leaf_count[max_depth])

if __name__ == '__main__':
    solve()