import sys
import math
from collections import defaultdict, deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        graph = defaultdict(list)
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        
        # Maximum antimatching is the maximum number of edges such that no two share a common endpoint
        # This is equivalent to finding the maximum matching in the line graph of the original graph
        # However, since the line graph is not directly available, we can use a bipartite matching approach
        
        # We can model this as a bipartite graph where each node is split into two parts: left and right
        # and edges are added between the two parts based on the original graph
        # Then, the maximum matching in this bipartite graph gives the maximum antimatching in the original graph
        
        # Create bipartite graph
        bipartite_graph = defaultdict(list)
        for u in graph:
            for v in graph[u]:
                if u < v:
                    bipartite_graph[u].append(v)
        
        # Use Hopcroft-Karp algorithm for maximum bipartite matching
        def hopcroft_karp():
            pair_u = [-1] * n
            pair_v = [-1] * n
            dist = [0] * n
            
            def bfs():
                queue = deque()
                for u in range(n):
                    if pair_u[u] == -1:
                        dist[u] = 0
                        queue.append(u)
                    else:
                        dist[u] = float('inf')
                dist_null = float('inf')
                while queue:
                    u = queue.popleft()
                    if dist[u] < dist_null:
                        for v in bipartite_graph[u]:
                            if pair_v[v] == -1:
                                dist_null = dist[u] + 1
                            elif dist[pair_v[v]] == float('inf'):
                                dist[pair_v[v]] = dist[u] + 1
                                queue.append(pair_v[v])
                return dist_null != float('inf')
            
            def dfs(u):
                for v in bipartite_graph[u]:
                    if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                        pair_u[u] = v
                        pair_v[v] = u
                        return True
                dist[u] = float('inf')
                return False
            
            result = 0
            while bfs():
                for u in range(n):
                    if pair_u[u] == -1:
                        if dfs(u):
                            result += 1
            return result
        
        max_antimatching = hopcroft_karp()
        results.append(str(max_antimatching))
    
    print('\n'.join(results))