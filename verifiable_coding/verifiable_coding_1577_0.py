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
    M = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N

    gears = [0] * (N + 1)
    for i in range(1, N + 1):
        gears[i] = A[i - 1]

    graph = defaultdict(list)
    parent = [0] * (N + 1)
    speed = [0] * (N + 1)
    visited = [False] * (N + 1)
    direction = [0] * (N + 1)
    blocked = [False] * (N + 1)

    def dfs(u, p):
        visited[u] = True
        parent[u] = p
        for v in graph[u]:
            if not visited[v]:
                direction[v] = -direction[u]
                dfs(v, u)
            else:
                if parent[v] != u and parent[u] != v:
                    blocked[u] = True
                    blocked[v] = True

    for _ in range(M):
        T = int(data[idx])
        idx += 1
        if T == 1:
            X = int(data[idx])
            idx += 1
            C = int(data[idx])
            idx += 1
            gears[X] = C
        elif T == 2:
            X = int(data[idx])
            idx += 1
            Y = int(data[idx])
            idx += 1
            graph[X].append(Y)
            graph[Y].append(X)
            dfs(X, 0)
            dfs(Y, 0)
        elif T == 3:
            X = int(data[idx])
            idx += 1
            Y = int(data[idx])
            idx += 1
            V = int(data[idx])
            idx += 1
            if blocked[Y]:
                print("0")
                continue
            if blocked[X]:
                print("0")
                continue
            if X == Y:
                print(f"{V}/{1}")
                continue
            if not blocked[X] and not blocked[Y]:
                speed[Y] = -speed[X] * gears[X] // gears[Y]
                print(f"{speed[Y]}/{1}")
            else:
                print("0")