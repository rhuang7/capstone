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
        for i in range(n):
            if len(adj[i]) == 1:
                leaves += 1
        
        # Calculate the maximum number of moves
        moves = 0
        while leaves >= k:
            # Find a node with at least k leaves connected to it
            for i in range(n):
                if len(adj[i]) == 1:
                    # This is a leaf, not a node with multiple leaves
                    continue
                # Count how many leaves are connected to this node
                cnt = 0
                for j in adj[i]:
                    if len(adj[j]) == 1:
                        cnt += 1
                if cnt >= k:
                    # Remove these k leaves
                    moves += 1
                    # Remove the k leaves and their edges
                    for j in adj[i]:
                        if len(adj[j]) == 1:
                            # This is a leaf
                            adj[i].remove(j)
                            adj[j].remove(i)
                            leaves -= 1
                    # Remove the node i (since it's no longer a leaf)
                    adj[i].clear()
                    del adj[i]
                    break
        results.append(str(moves))
    
    print('\n'.join(results))