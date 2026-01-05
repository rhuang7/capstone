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
        idx += 1
        p = list(map(int, data[idx:idx + N - 1]))
        idx += N - 1
        tree = defaultdict(list)
        for i in range(1, N):
            tree[p[i - 1]].append(i)
        # Compute the size of each subtree
        size = [0] * (N + 1)
        def dfs(u):
            size[u] = 1
            for v in tree[u]:
                dfs(v)
                size[u] += size[v]
        dfs(1)
        # Compute the maximum sum of MEX
        # For each node, the MEX of its subtree is the size of the subtree
        # Because if we assign 0 to the root, 1 to its child, etc., the MEX is the size
        # So the sum is the sum of sizes of all subtrees
        sum_mex = 0
        def dfs2(u):
            nonlocal sum_mex
            sum_mex += size[u]
            for v in tree[u]:
                dfs2(v)
        dfs2(1)
        results.append(sum_mex)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()