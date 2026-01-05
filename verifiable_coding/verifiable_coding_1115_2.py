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
        
        # Compute subtree sizes and depths
        size = [1] * N
        depth = [0] * N
        is_leaf = [True] * N
        
        def dfs(u, parent):
            is_leaf[u] = False
            for v in tree[u]:
                if v != parent:
                    depth[v] = depth[u] + 1
                    dfs(v, u)
                    size[u] += size[v]
                    is_leaf[u] = True
        
        dfs(0, -1)
        
        # For each node, compute the contribution of its value to the total profit
        # The contribution is A[i] * (number of paths that pass through i)
        # The number of paths that pass through i is (size of subtree of i) * (N - size of subtree of i)
        # But since we can permute the values, we want to assign the largest A[i] to the node with the largest (size * (N - size))
        # So we sort the nodes by (size * (N - size)) in descending order and assign the largest A[i] to the node with the largest value
        
        # Compute the contribution factor for each node
        contrib = [size[i] * (N - size[i]) for i in range(N)]
        
        # Sort nodes by contrib in descending order
        nodes = sorted(range(N), key=lambda x: -contrib[x])
        
        # Sort A in descending order
        A.sort(reverse=True)
        
        # Assign A[i] to nodes[i]
        total = 0
        for i in range(N):
            total = (total + A[i] * contrib[nodes[i]]) % MOD
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()