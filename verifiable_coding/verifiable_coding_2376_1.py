import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input.split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        adj = collections.defaultdict(list)
        for _ in range(n-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Compute degree of each node
        degree = [0] * n
        for u in range(n):
            degree[u] = len(adj[u])
        
        # Count number of leaves
        leaves = 0
        for u in range(n):
            if degree[u] == 1:
                leaves += 1
        
        # Compute maximum number of moves
        moves = 0
        while leaves >= k:
            # Find a node with at least k leaves connected to it
            found = False
            for u in range(n):
                if degree[u] >= k and sum(1 for v in adj[u] if degree[v] == 1) >= k:
                    # Remove k leaves
                    moves += 1
                    # Remove the k leaves
                    leaves -= k
                    # Decrease degree of the node
                    degree[u] -= k
                    # For each of the k leaves, they are no longer leaves
                    # So their degree is now 0 (they are removed)
                    # So we need to count them as removed
                    # But since we are removing them, we can just decrease the count of leaves
                    # and also decrease the degree of their neighbors
                    # However, since we are only counting leaves, and we are removing them, we can just subtract k from leaves
                    # and also decrease the degree of the node
                    # But we need to make sure that after this, the node is not a leaf anymore
                    # So we can just set its degree to 0
                    degree[u] = 0
                    found = True
                    break
            if not found:
                break
        
        results.append(str(moves))
    
    print('\n'.join(results))