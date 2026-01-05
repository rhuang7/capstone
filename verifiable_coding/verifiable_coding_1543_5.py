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
        m = int(data[idx+1])
        idx += 2
        sets = []
        for _ in range(m):
            vi = int(data[idx])
            idx += 1
            s = set(map(int, data[idx:idx+vi]))
            idx += vi
            sets.append(s)
        
        # Build the bipartite graph
        # Each element in X is a node on the left
        # Each set Si is a node on the right
        # There is an edge between element x and set Si if x is in Si
        # We need to find the minimum vertex cover in this bipartite graph
        # The minimum vertex cover is equal to the maximum matching (Konig's theorem)
        
        # Create adjacency list
        adj = [[] for _ in range(n)]
        for i in range(m):
            for x in sets[i]:
                adj[x].append(i)
        
        # Find maximum matching using Hopcroft-Karp algorithm
        def hopcroft_karp():
            pair_u = [-1] * n
            pair_v = [-1] * m
            dist = [0] * n
            
            def bfs():
                queue = []
                for u in range(n):
                    if pair_u[u] == -1:
                        dist[u] = 0
                        queue.append(u)
                    else:
                        dist[u] = float('inf')
                dist_null = float('inf')
                while queue:
                    u = queue.pop(0)
                    if dist[u] < dist_null:
                        for v in adj[u]:
                            if pair_v[v] == -1:
                                dist_null = dist[u] + 1
                            elif dist[pair_v[v]] == float('inf'):
                                dist[pair_v[v]] = dist[u] + 1
                                queue.append(pair_v[v])
                return dist_null != float('inf')
            
            def dfs(u):
                for v in adj[u]:
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
        
        max_matching = hopcroft_karp()
        results.append(str(max_matching))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()