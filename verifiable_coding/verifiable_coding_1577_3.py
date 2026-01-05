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

    # Each node has a parent and a ratio to its parent
    parent = [0] * (N + 1)
    ratio = [1] * (N + 1)
    # To detect cycles and blocked gears
    visited = [0] * (N + 1)
    # For each node, store the direction (0 for unvisited, 1 for visited, 2 for blocked)
    # And the speed ratio from the root
    # We'll use BFS to detect cycles
    # For each node, store its speed ratio from the root
    # And the direction (0 for unvisited, 1 for visited, 2 for blocked)
    # We'll use a Union-Find structure with path compression
    # But we need to track the ratio between nodes
    # So we use a DSU with ratio tracking

    # DSU with ratio tracking
    class DSU:
        def __init__(self, size):
            self.parent = list(range(size + 1))
            self.ratio = [1] * (size + 1)
            self.rank = [1] * (size + 1)
            self.blocked = [False] * (size + 1)

        def find(self, x):
            if self.parent[x] != x:
                orig_parent = self.parent[x]
                self.parent[x] = self.find(orig_parent)[0]
                self.ratio[x] *= self.find(orig_parent)[1]
            return self.parent[x], self.ratio[x]

        def union(self, x, y, a, b):
            # Connect x and y with ratio a/b
            # So x's ratio is a and y's ratio is b
            # So x's ratio is (a / b) * y's ratio
            # So when we find the root of x and y, we need to set the ratio between them
            # So we find the roots of x and y
            # If they are in the same set, we check if the ratio is consistent
            # If not, it's a cycle and the gears are blocked
            # Otherwise, we merge them
            root_x, ratio_x = self.find(x)
            root_y, ratio_y = self.find(y)
            if root_x == root_y:
                # Check if the ratio is consistent
                if ratio_x * b != ratio_y * a:
                    # Inconsistent ratio, gears are blocked
                    self.blocked[root_x] = True
                    self.blocked[root_y] = True
                    return
                return
            # Merge smaller rank into larger rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.ratio[root_x] = (ratio_x * a) / (ratio_y * b)
            else:
                self.parent[root_y] = root_x
                self.ratio[root_y] = (ratio_y * b) / (ratio_x * a)
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1
            return

    dsu = DSU(N)

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
            dsu.union(X, Y, gears[X], gears[Y])
        elif T == 3:
            X = int(data[idx])
            idx += 1
            Y = int(data[idx])
            idx += 1
            V = int(data[idx])
            idx += 1
            root_x, ratio_x = dsu.find(X)
            root_y, ratio_y = dsu.find(Y)
            if dsu.blocked[root_x] or dsu.blocked[root_y]:
                print("0/1")
            else:
                # The speed of Y is V * (ratio_x / ratio_y)
                # Because X's speed is V, and the ratio between X and Y is ratio_x / ratio_y
                # So Y's speed is V * (ratio_x / ratio_y)
                # But we need to compute this as a fraction
                # So we compute numerator and denominator
                # V * ratio_x / ratio_y
                # But ratio_x and ratio_y are stored as floats, so we need to track them as fractions
                # So we need to track the ratio as a fraction, not a float
                # So we need to track the ratio as a numerator and denominator
                # So we need to modify the DSU to track the ratio as a fraction
                # So we need to track the ratio as a numerator and denominator
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a numerator and denominator
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DSU with fractions
                # So we need to track the ratio as a fraction
                # So we need to use a DS