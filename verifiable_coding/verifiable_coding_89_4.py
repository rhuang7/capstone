import sys
import math
from collections import deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Build the BFS order tree
        # The BFS order is given, so we can reconstruct the tree structure
        # Each node's children are added in the order they appear in the BFS sequence
        # We need to find the minimum height tree that matches the BFS order
        
        # We can use a BFS-like approach to determine the depth of each node
        # The depth of a node is the level in the BFS traversal
        # The height of the tree is the maximum depth of any node
        
        # Create a dictionary to store the depth of each node
        depth = {}
        q = deque()
        q.append(a[0])
        depth[a[0]] = 0
        
        # We need to find the level of each node in the BFS traversal
        # We can do this by tracking the order of nodes in the BFS
        # The first node is at level 0
        # The next nodes are at level 1, then level 2, etc.
        # So, the level of a node is the number of times we have processed nodes before it
        
        # We can track the level of each node by keeping a counter
        level = 0
        level_count = 1  # Number of nodes at current level
        next_level_count = 0  # Number of nodes at next level
        
        for i in range(1, n):
            if i % level_count == 0:
                # All nodes at this level are processed
                level += 1
                level_count, next_level_count = next_level_count, 0
            # The current node is at the next level
            depth[a[i]] = level
        
        # The height of the tree is the maximum depth
        height = max(depth.values())
        results.append(str(height))
    
    print('\n'.join(results))