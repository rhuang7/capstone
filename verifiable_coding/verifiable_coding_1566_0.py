import sys
import math
from collections import defaultdict

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
            i = int(data[idx]) - 1
            j = int(data[idx+1]) - 1
            val = int(data[idx+2])
            idx += 3
            edges.append((i, j, val))
        # Build graph
        graph = defaultdict(list)
        for i, j, val in edges:
            if val == 0:
                graph[i].append((j, 0))
                graph[j].append((i, 0))
            else:
                graph[i].append((j, 1))
                graph[j].append((i, 1))
        # Check for consistency
        color = {}
        is_possible = True
        for start in range(N):
            if start not in color:
                stack = [(start, 0)]
                color[start] = 0
                while stack:
                    node, c = stack.pop()
                    for neighbor, val in graph[node]:
                        if neighbor in color:
                            if color[neighbor] != c ^ val:
                                is_possible = False
                                break
                        else:
                            color[neighbor] = c ^ val
                            stack.append((neighbor, c ^ val))
                    if not is_possible:
                        break
                if not is_possible:
                    break
        results.append("yes" if is_possible else "no")
    print('\n'.join(results))