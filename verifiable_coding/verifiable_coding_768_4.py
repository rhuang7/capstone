import sys
import math
from sys import stdin

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + N - 1]))
        idx += N - 1
        # Build tree
        tree = [[] for _ in range(N + 1)]
        for i in range(1, N):
            tree[p[i - 1]].append(i)
        # Compute size of each subtree
        size = [0] * (N + 1)
        def dfs(u):
            size[u] = 1
            for v in tree[u]:
                dfs(v)
                size[u] += size[v]
        dfs(1)
        # Compute maximum sum of MEX
        # The maximum sum is sum_{u=1 to N} (size[u] - 1)
        # Because the MEX of a subtree of size s is s if all numbers from 0 to s-1 are present
        # So the maximum sum is sum (size[u] - 1) for all u
        total = 0
        for i in range(1, N + 1):
            total += size[i] - 1
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()