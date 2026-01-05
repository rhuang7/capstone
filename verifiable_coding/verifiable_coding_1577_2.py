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

    # For each gear, store its connected gears and the ratio
    # We use a dictionary to store the connected gears and the ratio
    # Each gear has a parent and a ratio to its parent
    parent = [0] * (N + 1)
    ratio = [1] * (N + 1)
    blocked = [False] * (N + 1)

    def find(u):
        if parent[u] != u:
            # Path compression
            orig_parent = parent[u]
            parent[u] = find(orig_parent)
            ratio[u] *= ratio[orig_parent]
        return parent[u]

    def union(u, v):
        # Find roots of u and v
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return False
        # Check if the gears are in a cycle
        if blocked[root_u] or blocked[root_v]:
            blocked[root_u] = True
            blocked[root_v] = True
            return False
        # Merge the smaller tree into the larger one
        if ratio[root_u] * ratio[root_v] != -1:
            # The gears are in a cycle with conflicting directions
            blocked[root_u] = True
            blocked[root_v] = True
            return False
        # Merge
        parent[root_v] = root_u
        ratio[root_v] = -ratio[root_v] * ratio[u] / ratio[v]
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
            # Check if X and Y are in the same component
            root_x = find(X)
            root_y = find(Y)
            if root_x == root_y:
                continue
            # Check if they are in a cycle
            if blocked[root_x] or blocked[root_y]:
                continue
            # Check if the gears are in a cycle with conflicting directions
            if ratio[root_x] * ratio[root_y] != -1:
                blocked[root_x] = True
                blocked[root_y] = True
                continue
            # Union
            parent[root_y] = root_x
            ratio[root_y] = -ratio[root_y] * ratio[X] / ratio[Y]
        elif T == 3:
            X = int(data[idx])
            idx += 1
            Y = int(data[idx])
            idx += 1
            V = int(data[idx])
            idx += 1
            root_x = find(X)
            root_y = find(Y)
            if blocked[root_x] or blocked[root_y]:
                print("0/1")
                continue
            # Calculate the ratio between Y and X
            ratio_y_x = ratio[root_y] / ratio[root_x]
            # The speed of Y is V * ratio_y_x
            num = V * ratio_y_x
            den = 1
            # Simplify the fraction
            g = math.gcd(abs(num), den)
            num //= g
            den //= g
            print(f"{num}/{den}")

if __name__ == '__main__':
    solve()