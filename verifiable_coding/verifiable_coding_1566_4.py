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
        # Build graph
        graph = [[] for _ in range(N+1)]
        for i, j, val in edges:
            graph[i].append((j, val))
            graph[j].append((i, val))
        # Check for consistency
        # We need to assign values to nodes such that |A[i] - A[j]| = val
        # This is equivalent to a graph where edges have weights, and we need to assign values to nodes such that the difference between connected nodes is the edge weight
        # This is a problem of checking if the graph is bipartite with edge weights
        # We can model this as a bipartition problem with constraints
        # We can use BFS to assign values to nodes
        color = [None] * (N+1)
        is_possible = True
        for start in range(1, N+1):
            if color[start] is None:
                queue = [start]
                color[start] = 0
                while queue:
                    u = queue.pop(0)
                    for v, val in graph[u]:
                        if color[v] is None:
                            color[v] = color[u] ^ val
                            queue.append(v)
                        else:
                            if color[v] != color[u] ^ val:
                                is_possible = False
                                break
                    if not is_possible:
                        break
                if not is_possible:
                    break
        if is_possible:
            results.append("yes")
        else:
            results.append("no")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()