import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        adj = collections.defaultdict(list)
        for _ in range(n-1):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            adj[x].append(y)
            adj[y].append(x)
            idx += 2
        
        # Count the number of leaves
        leaves = 0
        for v in range(n):
            if len(adj[v]) == 1:
                leaves += 1
        
        # Calculate the maximum number of moves
        moves = 0
        while True:
            # Count the number of leaves
            current_leaves = 0
            for v in range(n):
                if len(adj[v]) == 1:
                    current_leaves += 1
            if current_leaves < k:
                break
            # Remove k leaves from a common node
            moves += 1
            # Find a node with at least k leaves connected to it
            found = False
            for v in range(n):
                if len(adj[v]) == 1:
                    continue
                cnt = 0
                for neighbor in adj[v]:
                    if len(adj[neighbor]) == 1:
                        cnt += 1
                if cnt >= k:
                    # Remove k leaves
                    for neighbor in adj[v]:
                        if len(adj[neighbor]) == 1:
                            adj[v].remove(neighbor)
                            adj[neighbor].remove(v)
                            # If the neighbor becomes a leaf, it will be counted in next iteration
                    found = True
                    break
            if not found:
                break
        
        results.append(str(moves))
    
    print('\n'.join(results))