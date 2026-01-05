import sys
import math
from collections import defaultdict, deque

def solve():
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
    # We'll use a Union-Find structure with path compression and union by rank
    # But since gears can be blocked, we need to track if a gear is blocked
    # We'll also track the ratio between gears in the same connected component
    # We'll use a dictionary to store the ratio from the root to each gear
    # And a dictionary to store the root of each gear
    parent = [i for i in range(N+1)]
    rank = [1] * (N+1)
    ratio = [1] * (N+1)  # ratio[i] is the ratio from the root to gear i
    blocked = [False] * (N+1)

    def find(u):
        if parent[u] != u:
            # Path compression
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        # Find roots
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return
        # Union by rank
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
            ratio[root_v] *= ratio[root_u] * (A[u] / A[v])
        else:
            parent[root_v] = root_u
            ratio[root_u] *= ratio[root_v] * (A[v] / A[u])
            rank[root_u] += rank[root_v]

    # For each query
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
            # Check if either gear is blocked
            if blocked[X] or blocked[Y]:
                blocked[X] = True
                blocked[Y] = True
                continue
            # Check if they are already connected
            if find(X) == find(Y):
                continue
            # Union them
            union(X, Y)
        elif T == 3:
            X = int(data[idx])
            idx += 1
            Y = int(data[idx])
            idx += 1
            V = int(data[idx])
            idx += 1
            # Check if gear Y is blocked
            if blocked[Y]:
                print("0")
                continue
            # Find the root of X
            root_x = find(X)
            # Check if X is blocked
            if blocked[X]:
                print("0")
                continue
            # Find the root of Y
            root_y = find(Y)
            # If X and Y are not in the same component
            if root_x != root_y:
                print("0")
                continue
            # Calculate the ratio from X to Y
            ratio_xy = ratio[root_x] * (A[X] / A[Y])
            speed = V * ratio_xy
            # Simplify the fraction
            numerator = speed
            denominator = 1
            if numerator == 0:
                print("0")
                continue
            g = math.gcd(abs(numerator), denominator)
            numerator //= g
            denominator //= g
            print(f"{numerator}/{denominator}")
        else:
            pass  # Invalid query type

if __name__ == '__main__':
    solve()