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
        # But since we are considering paths between leaves, we need to find the number of leaf paths that pass through each node
        
        # First, find the number of leaves
        leaves = []
        visited = [False] * N
        q = deque()
        for i in range(N):
            if len(tree[i]) == 1:
                leaves.append(i)
                q.append(i)
                visited[i] = True
        
        # Compute the number of paths that pass through each node
        # We use a post-order traversal to calculate the size of each subtree
        # and the number of paths that pass through each node
        # We also track the number of leaves in each subtree
        
        # We'll use a memoization approach
        # For each node, we'll store:
        # - size: number of nodes in the subtree
        # - leaf_count: number of leaves in the subtree
        # - path_count: number of paths that pass through this node
        
        # We'll perform a post-order traversal
        # We'll use a stack for iterative DFS
        
        # We'll also need to track which nodes have been visited
        # and their children
        
        # We'll use a visited array to track which nodes have been processed
        visited = [False] * N
        
        # We'll use a stack for DFS
        stack = []
        # We'll use a parent array to avoid revisiting the parent
        parent = [-1] * N
        
        # We'll use a dictionary to store the subtree information
        subtree = {}
        
        # We'll start from each leaf and perform a post-order traversal
        for leaf in leaves:
            # Mark the leaf as visited
            visited[leaf] = True
            # Push the leaf onto the stack
            stack.append((leaf, -1, False))
            
            while stack:
                node, p, processed = stack.pop()
                if processed:
                    # Process the node
                    # Initialize size and leaf_count
                    size = 1
                    leaf_count = 1 if len(tree[node]) == 1 else 0
                    path_count = 0
                    
                    # Iterate through children
                    for child in tree[node]:
                        if child == p:
                            continue
                        if not visited[child]:
                            # We need to process the child first
                            stack.append((node, p, True))
                            stack.append((child, node, False))
                            visited[child] = True
                            break
                    else:
                        # All children have been processed
                        # Now calculate size and leaf_count
                        for child in tree[node]:
                            if child == p:
                                continue
                            size += subtree[child]['size']
                            leaf_count += subtree[child]['leaf_count']
                            path_count += subtree[child]['path_count']
                        
                        # Now calculate the number of paths that pass through this node
                        # For each child, the number of paths that pass through this node is
                        # (number of leaves in the subtree of the child) * (number of leaves in the rest of the tree)
                        # But since we are considering paths between leaves, we need to count how many paths pass through this node
                        # For each child, the number of paths that pass through this node is (leaf_count_child) * (total_leaf_count - leaf_count_child)
                        # But we need to do this for all children
                        # However, since we are considering paths between leaves, the number of paths that pass through this node is
                        # sum over all children of (leaf_count_child * (total_leaf_count - leaf_count_child))
                        # But we need to do this for all children
                        # However, since we are doing a post-order traversal, we can accumulate this
                        # But since we are doing this for each node, we need to track the total number of leaves in the tree
                        # So we need to compute the total number of leaves in the tree
                        # But since we are starting from leaves, we can compute the total number of leaves
                        # as the number of leaves in the initial list
                        total_leaf_count = len(leaves)
                        
                        for child in tree[node]:
                            if child == p:
                                continue
                            if subtree[child]['leaf_count'] > 0:
                                path_count += subtree[child]['leaf_count'] * (total_leaf_count - subtree[child]['leaf_count'])
                        
                        # Store the subtree information
                        subtree[node] = {
                            'size': size,
                            'leaf_count': leaf_count,
                            'path_count': path_count
                        }
                else:
                    # Push the node back with processed=True
                    stack.append((node, p, True))
                    # Push children in reverse order to process them in the correct order
                    for child in reversed(tree[node]):
                        if child == p:
                            continue
                        if not visited[child]:
                            stack.append((child, node, False))
                            visited[child] = True
        
        # Now, for each node, we need to calculate the contribution of its value to the total sum
        # The contribution is (number of paths that pass through the node) * (value of the node)
        # But since each path is counted twice (once for each end), we need to multiply by 2
        # However, since we are considering paths between leaves, each path is counted once
        # So the contribution is (number of paths that pass through the node) * (value of the node)
        # But since each path is counted once, we need to multiply by 1
        
        total = 0
        for node in range(N):
            if subtree[node]['path_count'] > 0:
                total += A[node] * subtree[node]['path_count']
        
        results.append(total % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()