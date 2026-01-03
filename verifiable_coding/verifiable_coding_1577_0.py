import sys
import math
from collections import defaultdict, deque

def main():
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

    # For each gear, store its connected gears and the ratio
    # We use a Union-Find (Disjoint Set Union) structure to track connected components
    # But we also need to track the ratio of speed between gears in the component
    # We use a dictionary to store the ratio from the root to each gear
    parent = [i for i in range(N + 1)]
    rank = [1] * (N + 1)
    ratio = [1] * (N + 1)  # ratio[i] is the ratio of speed from root to gear i

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
            ratio[v_root] *= ratio[u_root] * (gears[u] / gears[v])
        else:
            parent[v_root] = u_root
            ratio[u_root] *= ratio[v_root] * (gears[v] / gears[u])
            if rank[u_root] == rank[v_root]:
                rank[u_root] += 1

    def get_ratio(u):
        root = find(u)
        return ratio[root] * (gears[u] / gears[root])

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
            union(X, Y)
        elif T == 3:
            X = int(data[idx])
            idx += 1
            Y = int(data[idx])
            idx += 1
            V = int(data[idx])
            idx += 1
            root_x = find(X)
            root_y = find(Y)
            if root_x != root_y:
                ratio_x = get_ratio(X)
                ratio_y = get_ratio(Y)
                speed = V * ratio_x / ratio_y
                numerator = speed * ratio_y
                denominator = ratio_y
                g = math.gcd(numerator, denominator)
                print(f"{numerator // g}/{denominator // g}")
            else:
                print("0")

if __name__ == '__main__':
    main()