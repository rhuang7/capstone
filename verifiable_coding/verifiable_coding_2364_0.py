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
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Dijkstra's algorithm to find shortest paths
        def dijkstra(start, end):
            dist = [float('inf')] * (n+1)
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
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
        
        # Find the shortest paths from a to b, b to c, and c to a
        # The optimal path is a -> b (shortest) and b -> c (shortest)
        # But we need to assign the prices such that the sum is minimized
        # So we need to assign the smallest prices to the edges on the shortest paths
        
        # Find the shortest path from a to b
        # We can use BFS since it's unweighted
        def bfs(start, end):
            visited = [False] * (n+1)
            queue = [start]
            visited[start] = True
            prev = [0] * (n+1)
            while queue:
                u = queue.pop(0)
                if u == end:
                    break
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        prev[v] = u
                        queue.append(v)
            # Reconstruct path
            path = []
            current = end
            while current != start:
                path.append(current)
                current = prev[current]
            path.append(start)
            path.reverse()
            return path
        
        path_a_b = bfs(a, b)
        path_b_c = bfs(b, c)
        path_c_a = bfs(c, a)
        
        # Find all edges on the shortest paths
        # For each path, collect the edges
        def get_edges(path):
            edges = set()
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i+1]
                if u < v:
                    edges.add((u, v))
                else:
                    edges.add((v, u))
            return edges
        
        edges_ab = get_edges(path_a_b)
        edges_bc = get_edges(path_b_c)
        edges_ca = get_edges(path_c_a)
        
        # Combine all edges on the shortest paths
        all_edges = edges_ab.union(edges_bc).union(edges_ca)
        
        # Sort the prices and assign the smallest ones to the edges on the shortest paths
        p.sort()
        # Assign the smallest prices to the edges on the shortest paths
        # The number of edges on the shortest paths is len(all_edges)
        # The remaining edges get the larger prices
        # But since we want to minimize the total cost, we should assign the smallest prices to the edges on the shortest paths
        # So we take the first len(all_edges) prices and assign them to the edges on the shortest paths
        # The rest get the larger prices
        
        # The total cost is the sum of the prices assigned to the edges on the shortest paths
        # But since we want to minimize the total cost, we assign the smallest prices to the edges on the shortest paths
        # So we take the first len(all_edges) prices and assign them to the edges on the shortest paths
        # The rest get the larger prices
        # But since we are only concerned with the sum of the prices on the shortest paths, we just need to sum the first len(all_edges) prices
        
        total = sum(p[:len(all_edges)])
        results.append(str(total))
    
    print('\n'.join(results))