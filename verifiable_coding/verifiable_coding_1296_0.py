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
        adj = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        A = int(data[idx])
        idx += 1
        
        # Build the tree and find the Euler Tour
        # Perform a DFS to find the order of traversal
        visited = [False] * (N + 1)
        order = []
        parent = [0] * (N + 1)
        def dfs(u, p):
            visited[u] = True
            parent[u] = p
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    dfs(v, u)
        dfs(A, -1)
        
        # The order is the traversal order from A, but we need to find the number of ways to traverse the tree
        # The number of ways is (number of children of root) * (number of ways for each subtree)
        # We need to compute the factorial of (N-1) and divide by the product of (size of each subtree - 1)!
        # But since we are working modulo 1e9+7, we need to use modular inverses
        
        # Compute factorial and inverse factorial
        max_n = N
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Compute the number of ways
        def dfs_count(u):
            cnt = 1
            for v in adj[u]:
                if v != parent[u]:
                    cnt = cnt * dfs_count(v) % MOD
            return cnt
        
        # The number of ways is (number of children of root) * (product of (size of each subtree - 1)!)
        # But we need to compute the product of (size of each subtree - 1)! and multiply by (number of children of root)!
        # So we need to compute the size of each subtree
        size = [1] * (N + 1)
        def dfs_size(u):
            for v in adj[u]:
                if v != parent[u]:
                    dfs_size(v)
                    size[u] += size[v]
        dfs_size(A)
        
        # Compute the product of (size of each subtree - 1)!
        product = 1
        for v in adj[A]:
            if v != parent[A]:
                product = product * inv_fact[size[v] - 1] % MOD
        
        # The number of ways is (number of children of root)! * product
        num_children = len(adj[A]) - 1
        res = fact[num_children] * product % MOD
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()