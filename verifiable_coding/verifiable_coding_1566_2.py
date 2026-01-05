import sys
import math
from collections import defaultdict

def solve():
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
        constraints = []
        for __ in range(Q):
            i = int(data[idx])
            j = int(data[idx+1])
            val = int(data[idx+2])
            idx += 3
            constraints.append((i-1, j-1, val))
        # Build adjacency list
        graph = defaultdict(list)
        for i, j, val in constraints:
            if i != j:
                graph[i].append((j, val))
                graph[j].append((i, val))
        # Check for contradictions
        color = [-1] * N
        is_bipartite = True
        for start in range(N):
            if color[start] == -1:
                queue = [(start, 0)]
                color[start] = 0
                while queue:
                    node, c = queue.pop()
                    for neighbor, val in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - c
                            queue.append((neighbor, 1 - c))
                        else:
                            if color[neighbor] == c:
                                is_bipartite = False
                                break
                    if not is_bipartite:
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            results.append("no")
            continue
        # Check if all entries are consistent
        valid = True
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                # Check if the value is consistent with the color difference
                if (color[i] - color[j]) % 2 == 0:
                    if (i, j) in constraints:
                        if constraints[(i, j)][2] != 0:
                            valid = False
                            break
                    else:
                        if (i, j) in constraints:
                            if constraints[(i, j)][2] != 0:
                                valid = False
                                break
                        else:
                            if (j, i) in constraints:
                                if constraints[(j, i)][2] != 0:
                                    valid = False
                                    break
                else:
                    if (i, j) in constraints:
                        if constraints[(i, j)][2] != 1:
                            valid = False
                            break
                    else:
                        if (j, i) in constraints:
                            if constraints[(j, i)][2] != 1:
                                valid = False
                                break
            if not valid:
                break
        if valid:
            results.append("yes")
        else:
            results.append("no")
    print('\n'.join(results))