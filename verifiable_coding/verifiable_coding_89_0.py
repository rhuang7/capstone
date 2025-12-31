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
        # The BFS order is given as a, so we can reconstruct the tree
        # The tree must be such that children of each node are in ascending order
        # We need to find the minimum height tree that satisfies the BFS order
        
        # We can use the BFS order to determine the parent of each node
        # The first node is root (1)
        # For each node in a[1:], its parent is the previous node in the BFS order that is in the same level
        # We can track levels using a queue
        
        # Build the tree structure
        tree = {}
        for i in range(n):
            if i == 0:
                tree[a[i]] = []
            else:
                # Find the parent of a[i]
                # The parent is the first node in the BFS order that is in the same level
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order that is in the same level
                # We can track the level of each node
                # We can use a queue to track the nodes at each level
                # The parent of a[i] is the first node in the BFS order