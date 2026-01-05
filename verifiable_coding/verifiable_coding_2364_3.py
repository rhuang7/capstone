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
            edges.append((u, v))
            idx += 2
        
        # Build adjacency list
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Dijkstra to find shortest paths
        def dijkstra(start, end):
            dist = [float('inf')] * (n+1)
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
        
        # Find the shortest paths
        path_a_b = dist_a[b]
        path_b_c = dist_b[c]
        path_c_a = dist_c[a]
        
        # Total number of edges in the paths
        total_edges = path_a_b + path_b_c + path_c_a
        
        # Sort the prices
        p.sort()
        
        # Assign the smallest prices to the paths
        # The shortest path from a to b will have the smallest edges
        # The shortest path from b to c will have the next smallest
        # The shortest path from c to a will have the largest
        # So assign the smallest prices to the shortest paths
        # Sort the paths by length
        paths = [
            (path_a_b, "a->b"),
            (path_b_c, "b->c"),
            (path_c_a, "c->a")
        ]
        paths.sort()
        
        # Assign prices
        price_a_b = 0
        price_b_c = 0
        price_c_a = 0
        
        # Assign the smallest prices to the shortest paths
        for i in range(len(paths)):
            count = paths[i][0]
            for j in range(i * count, (i + 1) * count):
                if i == 0:
                    price_a_b += p[j]
                elif i == 1:
                    price_b_c += p[j]
                else:
                    price_c_a += p[j]
        
        total_cost = price_a_b + price_b_c + price_c_a
        results.append(str(total_cost))
    
    print('\n'.join(results))