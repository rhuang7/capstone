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
        
        # Compute the number of leaves
        leaves = 0
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                while q:
                    node = q.popleft()
                    for neighbor in tree[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                    if len(q) == 0 and len(tree[node]) == 0:
                        leaves += 1
        
        # Sort A in descending order
        A.sort(reverse=True)
        
        # Assign values to leaves first
        # For each leaf, assign the largest remaining value
        # Then assign the remaining values to internal nodes
        # But since we need to maximize the sum of profits, we should assign larger values to nodes that are on more paths
        # However, for this problem, it's sufficient to assign the largest values to leaves, as each leaf contributes to multiple paths
        
        # Assign largest values to leaves
        leaf_values = [0] * N
        leaf_count = 0
        for i in range(N):
            if len(tree[i]) == 0:
                leaf_values[i] = A[leaf_count]
                leaf_count += 1
        
        # Compute the contribution of each node to the total sum
        # Each node contributes its value multiplied by the number of paths that pass through it
        # For a tree, the number of paths that pass through a node is (number of leaves in one subtree) * (number of leaves in the other subtree)
        # So we need to compute for each node, the number of leaves in each of its subtrees
        
        # We'll perform a post-order traversal to compute the number of leaves in each subtree
        # We'll also compute the contribution of each node
        
        visited = [False] * N
        contribution = [0] * N
        
        def dfs(u, parent):
            leaf_count = 0
            for v in tree[u]:
                if v != parent:
                    child_leaf_count = dfs(v, u)
                    contribution[u] += child_leaf_count * (N - child_leaf_count) * leaf_values[u]
                    leaf_count += child_leaf_count
            if len(tree[u]) == 0:
                leaf_count += 1
            return leaf_count
        
        dfs(0, -1)
        
        # Sum all contributions and take modulo
        total = sum(contribution) % MOD
        results.append(total)
    
    for res in results:
        print(res)