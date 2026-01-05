import sys
import math
from collections import defaultdict

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    traffic = [0] * (N + 1)
    for i in range(1, N + 1):
        traffic[i] = int(data[idx])
        idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # We need to find the maximum independent set in a tree where nodes have weights
    # This is a classic problem that can be solved with dynamic programming on trees
    
    # We'll perform a post-order traversal and for each node, store two values:
    # 1. The maximum weight if we select the node
    # 2. The maximum weight if we don't select the node
    
    # To handle the tree, we'll root it at node 1 and perform DFS
    
    # To avoid recursion stack overflow, we'll use an iterative DFS approach
    
    # We'll also need to track the parent of each node to avoid revisiting the parent
    
    # We'll use a stack for DFS
    stack = [(1, 0, False)]
    parent = [0] * (N + 1)
    
    # We'll store the DP values in two arrays
    select = [0] * (N + 1)
    not_select = [0] * (N + 1)
    
    while stack:
        node, p, visited = stack.pop()
        if visited:
            # Process the node after children are processed
            select[node] = traffic[node]
            for child in adj[node]:
                if child != p:
                    select[node] += not_select[child]
            not_select[node] = 0
            for child in adj[node]:
                if child != p:
                    not_select[node] += select[child]
            continue
        parent[node] = p
        stack.append((node, p, True))
        for child in adj[node]:
            if child != p:
                stack.append((child, node, False))
    
    print(max(select[1], not_select[1]))