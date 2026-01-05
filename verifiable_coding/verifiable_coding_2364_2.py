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
        
        # Dijkstra to find shortest path from a to b
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
        
        dist_ab = dijkstra(a, b)
        dist_bc = dijkstra(b, c)
        
        # Find the shortest paths from a to b and b to c
        # Now, we need to assign the prices to edges such that the total cost is minimized
        # We need to assign the largest prices to the edges that are on the shortest paths
        # So we need to find all edges on the shortest path from a to b and from b to c
        
        # Find edges on shortest path from a to b
        def get_edges_on_shortest_path(start, end):
            visited = [False] * (n+1)
            prev = [None] * (n+1)
            dist = dijkstra(start, end)
            q = [end]
            visited[end] = True
            while q:
                u = q.pop(0)
                for v in adj[u]:
                    if not visited[v] and dist[v] == dist[u] - 1:
                        prev[v] = u
                        visited[v] = True
                        q.append(v)
            # Reconstruct path
            path = []
            u = end
            while u != start:
                path.append(u)
                u = prev[u]
            path.append(start)
            path.reverse()
            # Find edges on this path
            edges_on_path = []
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i+1]
                for edge in edges:
                    if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
                        edges_on_path.append(edge)
                        break
            return edges_on_path
        
        edges_ab = get_edges_on_shortest_path(a, b)
        edges_bc = get_edges_on_shortest_path(b, c)
        
        # Assign the largest prices to the edges on the shortest paths
        # Sort prices in descending order
        p.sort(reverse=True)
        # Assign the largest prices to the edges on the shortest paths
        # We need to assign the largest prices to the edges on the shortest paths
        # So we need to count the number of edges on the shortest paths
        count_ab = len(edges_ab)
        count_bc = len(edges_bc)
        # But we need to make sure that we don't double count the edge between b and itself
        # So we need to check if there is an edge between b and itself (but there isn't)
        # So we can safely add the counts
        total_edges = count_ab + count_bc
        # Assign the largest 'total_edges' prices to the edges on the shortest paths
        # The rest can be assigned to other edges
        # The total cost is the sum of the largest 'total_edges' prices
        total_cost = sum(p[:total_edges])
        results.append(str(total_cost))
    
    print('\n'.join(results))