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
        
        # Build the tree
        tree = defaultdict(list)
        for i in range(1, N):
            tree[p[i - 1]].append(i)
        
        # Compute the maximum sum of MEX
        # The maximum sum is N * (N - 1) // 2
        # Because each node contributes at most (size of subtree - 1)
        # But this is not correct, need to compute properly
        # Correct approach: for each node, the MEX of its subtree is the number of nodes in the subtree
        # So the maximum sum is the sum of the sizes of all subtrees
        
        # Compute sizes of all subtrees
        size = [0] * (N + 1)
        
        def dfs(u):
            size[u] = 1
            for v in tree[u]:
                dfs(v)
                size[u] += size[v]
        
        dfs(1)
        
        total = sum(size[1:])
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()