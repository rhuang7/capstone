import sys
import math
from sys import stdin
input = sys.stdin.buffer.read
MOD = 10**9 + 7

def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        A = int(data[idx])
        idx += 1
        
        # Compute the number of ways to traverse the tree
        # The tree is rooted at A, and we need to count the number of ways to traverse all nodes
        # This is equivalent to the number of linear extensions of the tree rooted at A
        # The number of ways is (product of (size of each subtree - 1)!) 
        # We use DFS to compute the sizes of subtrees and compute the product
        
        # Compute subtree sizes and factorials
        fact = [1] * (N + 1)
        for i in range(2, N + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        visited = [False] * (N + 1)
        def dfs(u, parent):
            visited[u] = True
            size = 1
            for v in adj[u]:
                if v != parent and not visited[v]:
                    size += dfs(v, u)
            if u != A:
                # Multiply by (size - 1)!
                size -= 1
                res = fact[size] % MOD
                results.append(res)
            return size
        
        dfs(A, -1)
        
        # Multiply all the results
        res = 1
        for val in results:
            res = res * val % MOD
        results[-1] = res
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()