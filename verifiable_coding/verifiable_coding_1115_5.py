import sys
import math
from collections import defaultdict, deque

MOD = 10**9 + 7

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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Compute the contribution of each node to the total sum
        # The contribution of a node is A[i] multiplied by the number of paths that pass through it
        # For a tree, the number of paths that pass through a node is (size of subtree) * (N - size of subtree)
        # We need to compute this for each node
        
        # First, compute the size of each subtree
        size = [1] * N
        visited = [False] * N
        
        def dfs(u, parent):
            for v in tree[u]:
                if v != parent:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(0, -1)
        
        # Now compute the contribution of each node
        contribution = [0] * N
        for u in range(N):
            contribution[u] = A[u] * size[u] * (N - size[u])
        
        # Sum all contributions and take modulo
        total = sum(contribution) % MOD
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()