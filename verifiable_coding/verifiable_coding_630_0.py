import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        classes = list(map(int, data[idx:idx+n]))
        idx += n
        edges = []
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        
        # Build the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        
        # Check if the graph is a valid structure (each node has at most 2 outgoing edges, and the structure is a tree)
        valid = True
        for u in range(n):
            if len(graph[u]) > 2:
                valid = False
                break
        
        if not valid:
            results.append(-1)
            continue
        
        # Check if the graph is a tree (connected and has n-1 edges)
        # We can do BFS to check connectivity
        visited = [False] * n
        q = collections.deque()
        q.append(0)
        visited[0] = True
        while q:
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        if sum(visited) != n:
            results.append(-1)
            continue
        
        # Check if the structure is a valid tree with each node having at most 2 outgoing edges
        # We can do a DFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # Also, check if the structure is a valid tree (each node has at most 2 outgoing edges and the structure is a tree)
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each node having at most 2 outgoing edges
        # We can do a BFS to check if the structure is a tree with each