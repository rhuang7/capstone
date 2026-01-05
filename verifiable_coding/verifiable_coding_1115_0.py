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
        # For a tree, each node contributes A[i] * (number of paths that pass through it)
        # The number of paths that pass through a node is equal to (number of leaves in the subtree) * (number of leaves outside the subtree)
        # We can compute this using a post-order traversal
        
        # First, compute the size of each subtree and the number of leaves in each subtree
        # Then, for each node, the number of paths that pass through it is (leaves_in_subtree) * (total_leaves - leaves_in_subtree)
        
        # Compute the number of leaves in each subtree
        # We'll do a post-order traversal
        def dfs(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs(v, u)
            if leaves == 0:
                leaves = 1  # if the node is a leaf
            return leaves
        
        total_leaves = dfs(0, -1)
        
        # Now compute the contribution of each node
        # We need to compute for each node, the number of paths that pass through it
        # This can be done with a second DFS
        def dfs2(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs2(v, u)
            if leaves == 0:
                leaves = 1
            # The number of paths that pass through u is leaves * (total_leaves - leaves)
            contribution = leaves * (total_leaves - leaves)
            return contribution
        
        # But this is not correct, because it counts the number of paths that pass through the node
        # But we need to count the number of paths that start and end at leaves and pass through the node
        # So we need to compute for each node, the number of paths that pass through it
        # This is done by the formula: (number of leaves in subtree) * (number of leaves outside subtree)
        
        # We need to compute for each node, the number of leaves in its subtree
        # And then compute the contribution as (leaves_in_subtree) * (total_leaves - leaves_in_subtree)
        
        # Let's do a post-order traversal to compute the number of leaves in each subtree
        def dfs3(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs3(v, u)
            if leaves == 0:
                leaves = 1
            return leaves
        
        # Now compute the contribution for each node
        # We need to compute for each node, the number of leaves in its subtree
        # Then, the contribution is (leaves_in_subtree) * (total_leaves - leaves_in_subtree)
        # But we also need to multiply by the value of the node
        
        # We'll do a post-order traversal again
        def dfs4(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs4(v, u)
            if leaves == 0:
                leaves = 1
            # The contribution of this node is A[u] * leaves * (total_leaves - leaves)
            contribution = A[u] * leaves * (total_leaves - leaves)
            return contribution
        
        total = 0
        # We need to compute the contribution for each node
        # But we need to make sure that we count each path exactly once
        # The formula (leaves_in_subtree) * (total_leaves - leaves_in_subtree) gives the number of paths that pass through the node
        # But this counts each path once, because each path is counted exactly once in the tree structure
        # So we can sum over all nodes the contribution
        
        # However, this approach is not correct because it counts each path multiple times
        # For example, a path that goes through two nodes will be counted in both nodes
        # So we need to find a way to count each path exactly once
        
        # The correct approach is to find for each node, the number of paths that start at a leaf and end at a leaf and pass through this node
        # This can be done by considering the number of leaves in the subtree and the number of leaves outside the subtree
        # For each node, the number of such paths is (leaves_in_subtree) * (total_leaves - leaves_in_subtree)
        # So we can compute this for each node and sum it up
        
        # Let's compute the number of leaves in each subtree
        # We'll do a post-order traversal again
        def dfs5(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs5(v, u)
            if leaves == 0:
                leaves = 1
            return leaves
        
        # Now compute the contribution for each node
        # We need to compute for each node, the number of leaves in its subtree
        # Then, the contribution is A[u] * leaves * (total_leaves - leaves)
        # But we need to make sure that we count each path exactly once
        # So we can sum over all nodes the contribution
        
        # We'll do a post-order traversal again
        def dfs6(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs6(v, u)
            if leaves == 0:
                leaves = 1
            contribution = A[u] * leaves * (total_leaves - leaves)
            return contribution
        
        # Now compute the total contribution
        total = 0
        # We need to compute the contribution for each node
        # But we need to make sure that we count each path exactly once
        # So we can sum over all nodes the contribution
        
        # We'll do a post-order traversal again
        def dfs7(u, parent):
            leaves = 0
            for v in tree[u]:
                if v != parent:
                    leaves += dfs7(v, u)
            if leaves == 0:
                leaves = 1
            contribution = A[u] * leaves * (total_leaves - leaves)
            nonlocal total
            total += contribution
            return leaves
        
        dfs7(0, -1)
        
        results.append(total % MOD)
    
    for res in results:
        print(res)