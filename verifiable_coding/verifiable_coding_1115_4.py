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
        
        # Compute the contribution of each node
        # We need to find the number of paths that pass through each node
        # For a tree, the number of paths that pass through a node is (size of subtree) * (N - size of subtree)
        # But since we are considering paths between leaves, we need to count the number of leaf paths that pass through each node
        
        # First, compute the size of each subtree
        size = [1] * N
        visited = [False] * N
        
        def dfs(u, parent):
            visited[u] = True
            for v in tree[u]:
                if not visited[v]:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(0, -1)
        
        # Now, compute the number of leaf paths that pass through each node
        # We need to find the number of leaf paths that pass through each node
        # For each node, the number of leaf paths passing through it is (number of leaves in its subtree) * (number of leaves outside its subtree)
        
        # First, compute the number of leaves in each subtree
        leaves = [0] * N
        visited = [False] * N
        
        def dfs_leaves(u, parent):
            visited[u] = True
            for v in tree[u]:
                if not visited[v]:
                    dfs_leaves(v, u)
                    leaves[u] += leaves[v]
            # If the node is a leaf (has no children except parent)
            if len(tree[u]) == 1 and u != 0:
                leaves[u] = 1
        
        dfs_leaves(0, -1)
        
        # Now, compute the number of leaf paths passing through each node
        # For each node, the number of leaf paths passing through it is leaves[u] * (total_leaves - leaves[u])
        total_leaves = sum(leaves)
        contrib = [0] * N
        
        def dfs_contrib(u, parent):
            for v in tree[u]:
                if v != parent:
                    contrib[u] += leaves[v] * (total_leaves - leaves[v])
                    dfs_contrib(v, u)
        
        dfs_contrib(0, -1)
        
        # Now, compute the maximum sum of profits
        # We need to assign the values to the nodes such that the nodes with higher contribution get higher values
        # Sort the nodes by their contribution in descending order
        nodes = list(range(N))
        nodes.sort(key=lambda x: -contrib[x])
        
        # Assign values to nodes in the sorted order
        res = 0
        for i in range(N):
            res = (res + A[i] * contrib[nodes[i]]) % MOD
        
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()