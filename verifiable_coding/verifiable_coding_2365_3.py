import sys

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
        idx += 1
        segments = []
        for _ in range(n-1):
            k = int(data[idx])
            idx += 1
            seg = list(map(int, data[idx:idx+k]))
            idx += k
            segments.append(seg)
        
        # Build a graph of possible positions
        # Each node is a number from 1 to n
        # Edges represent possible positions in the permutation
        graph = {i: [] for i in range(1, n+1)}
        
        # For each segment, add edges between elements
        for seg in segments:
            for i in range(len(seg)):
                for j in range(i+1, len(seg)):
                    a = seg[i]
                    b = seg[j]
                    graph[a].append(b)
                    graph[b].append(a)
        
        # Find the permutation using BFS starting from the smallest number
        # The permutation is the order in which nodes are visited in BFS
        # The first node is the smallest one (1)
        from collections import deque
        visited = [False] * (n + 1)
        q = deque()
        q.append(1)
        visited[1] = True
        perm = []
        
        while q:
            u = q.popleft()
            perm.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        results.append(' '.join(map(str, perm)))
    
    print('\n'.join(results))