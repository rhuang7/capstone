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
        graph = [[] for _ in range(N)]
        for __ in range(Q):
            i = int(data[idx]) - 1
            j = int(data[idx+1]) - 1
            val = int(data[idx+2])
            idx += 3
            if val == 0:
                graph[i].append(j)
                graph[j].append(i)
            else:
                graph[i].append(j)
                graph[j].append(i)
        # Check if the graph is bipartite
        color = [-1] * N
        is_bipartite = True
        for start in range(N):
            if color[start] == -1:
                queue = [start]
                color[start] = 0
                while queue:
                    u = queue.pop(0)
                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = color[u] ^ 1
                            queue.append(v)
                        else:
                            if color[v] == color[u]:
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