import sys
import heapq

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
        a = int(data[idx+2])
        b = int(data[idx+3])
        c = int(data[idx+4])
        idx += 5
        p = list(map(int, data[idx:idx+m]))
        idx += m
        
        edges = []
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            idx += 2
            edges.append((u, v))
        
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Dijkstra to find shortest paths
        def dijkstra(start, end):
            dist = [float('inf')] * (n + 1)
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if u == end:
                    break
                if d > dist[u]:
                    continue
                for v in adj[u]:
                    if dist[v] > d + 1:
                        dist[v] = d + 1
                        heapq.heappush(heap, (dist[v], v))
            return dist
        
        dist_a = dijkstra(a, b)
        dist_b = dijkstra(b, c)
        dist_c = dijkstra(c, a)
        
        # Find the three shortest paths
        path_a_b = dist_a[b]
        path_b_c = dist_b[c]
        path_c_a = dist_c[a]
        
        # Sort the prices
        p.sort()
        
        # Assign the smallest prices to the shortest paths
        # The total cost is the sum of the first (path_a_b + path_b_c) prices
        total = sum(p[:path_a_b + path_b_c])
        results.append(str(total))
    
    print('\n'.join(results))