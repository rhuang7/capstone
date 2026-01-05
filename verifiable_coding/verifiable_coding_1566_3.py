import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        edges = []
        for __ in range(Q):
            i = int(data[idx])
            j = int(data[idx+1])
            val = int(data[idx+2])
            idx += 3
            edges.append((i, j, val))
        # Build adjacency list
        graph = [[] for _ in range(N+1)]
        for i, j, val in edges:
            graph[i].append((j, val))
            graph[j].append((i, val))
        # Check if the graph is bipartite
        color = [-1] * (N+1)
        is_bipartite = True
        for start in range(1, N+1):
            if color[start] == -1:
                queue = [start]
                color[start] = 0
                while queue:
                    u = queue.pop(0)
                    for v, val in graph[u]:
                        if color[v] == -1:
                            color[v] = color[u] ^ val
                            queue.append(v)
                        else:
                            if color[v] != color[u] ^ val:
                                is_bipartite = False
                                break
                    if not is_bipartite:
                        break
                if not is_bipartite:
                    break
        if is_bipartite:
            results.append("yes")
        else:
            results.append("no")
    print("\n".join(results))