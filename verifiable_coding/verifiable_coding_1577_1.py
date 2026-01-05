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
    for i in range(1, N+1):
        gears[i] = A[i-1]

    # Each gear has a parent and a ratio to its parent
    parent = [0] * (N + 1)
    ratio = [1] * (N + 1)
    blocked = [False] * (N + 1)

    def find(u):
        if parent[u] != u:
            orig_parent = parent[u]
            parent[u] = find(parent[u])[0]
            ratio[u] *= ratio[orig_parent]
        return (parent[u], ratio[u])

    def union(u, v):
        pu, ru = find(u)
        pv, rv = find(v)
        if pu == pv:
            return False
        parent[pu] = pv
        ratio[pu] = -ru * rv
        return True

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
            # Check if either is blocked
            if blocked[X] or blocked[Y]:
                blocked[X] = True
                blocked[Y] = True
                continue
            # Check if they are in the same component
            pu, ru = find(X)
            pv, rv = find(Y)
            if pu == pv:
                # Already connected, but check if it's a valid connection
                # If the ratio is not consistent, it's a contradiction
                # So we need to check if ru * rv == -1
                # If not, then it's a contradiction and both are blocked
                if ru * rv != -1:
                    blocked[X] = True
                    blocked[Y] = True
                continue
            # Connect them
            parent[pu] = pv
            ratio[pu] = -ru * rv
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
            px, rx = find(X)
            py, ry = find(Y)
            if px != py:
                # Compute the speed
                speed = V * rx * ry
                # Simplify the fraction
                g = math.gcd(speed, 1)
                num = speed // g
                den = 1 // g
                print(f"{num}/{den}")
            else:
                print("0")