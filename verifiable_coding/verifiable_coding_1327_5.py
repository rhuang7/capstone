import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        v = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute for each node, the best paths to and from other nodes
        # We'll use BFS for shortest path and DFS for longest path
        
        # For each query, we need to find:
        # 1. Minimum cost from x to y
        # 2. Maximum length of such path
        
        # Since N and Q are large, we need an efficient way to answer queries
        # We'll use BFS for minimum cost and DFS for maximum length
        
        # Precompute adjacency list
        adj = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    cost = abs(v[j] - v[i]) + (j - i)
                    adj[i].append((j, cost))
        
        # Precompute for each node, the minimum cost to all other nodes
        # Using Dijkstra's algorithm
        min_cost = [ [float('inf')] * N for _ in range(N) ]
        for i in range(N):
            min_cost[i][i] = 0
            heap = [(0, i)]
            visited = [False] * N
            while heap:
                dist, u = heapq.heappop(heap)
                if visited[u]:
                    continue
                visited[u] = True
                for v, w in adj[u]:
                    if dist + w < min_cost[i][v]:
                        min_cost[i][v] = dist + w
                        heapq.heappush(heap, (min_cost[i][v], v))
        
        # Precompute for each node, the maximum length of path to all other nodes
        # Using BFS
        max_len = [ [0] * N for _ in range(N) ]
        for i in range(N):
            queue = deque()
            queue.append((i, 0))
            visited = [False] * N
            visited[i] = True
            while queue:
                u, l = queue.popleft()
                for v, w in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append((v, l + 1))
                        max_len[i][v] = l + 1
        
        # Process queries
        for __ in range(Q):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            if x == y:
                results.append(f"{0} 1")
                continue
            min_c = min_cost[x][y]
            max_l = max_len[x][y]
            results.append(f"{min_c} {max_l}")
    
    print("\n".join(results))