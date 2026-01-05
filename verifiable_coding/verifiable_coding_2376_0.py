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
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Count the number of leaves
        leaves = 0
        for u in range(n):
            if len(adj[u]) == 1:
                leaves += 1
        
        # Calculate the maximum number of moves
        moves = 0
        while leaves >= k:
            # Find a node with at least k leaves connected to it
            found = False
            for u in range(n):
                if len(adj[u]) == 1:
                    # This is a leaf, not a candidate
                    continue
                cnt = 0
                for v in adj[u]:
                    if len(adj[v]) == 1:
                        cnt += 1
                if cnt >= k:
                    # Remove k leaves
                    moves += 1
                    # Remove the k leaves
                    for v in adj[u]:
                        if len(adj[v]) == 1:
                            leaves -= 1
                            # Remove the edge
                            adj[u].remove(v)
                            adj[v].remove(u)
                    # Remove the node u
                    for v in adj[u]:
                        adj[v].remove(u)
                    adj[u].clear()
                    del adj[u]
                    found = True
                    break
            if not found:
                break
        
        results.append(str(moves))
    
    print('\n'.join(results))