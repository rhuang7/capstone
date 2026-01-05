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
            s = list(map(int, data[idx:idx+vi]))
            idx += vi
            sets.append(s)
        
        # Build the bipartite graph
        # Each element in X is a node on the left
        # Each set Si is a node on the right
        # There is an edge between element x and set Si if x is in Si
        # We need to find the minimum vertex cover of this bipartite graph
        # The minimum vertex cover is equal to the maximum matching (Konig's theorem)
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for i in range(m):
            for x in sets[i]:
                adj[x].append(i)
        
        # Find maximum matching using DFS
        def bpm(u, visited, match_to):
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if match_to[v] == -1 or bpm(match_to[v], visited, match_to):
                        match_to[v] = u
                        return True
            return False
        
        match_to = [-1] * m
        result = 0
        for u in range(n):
            visited = [False] * m
            if bpm(u, visited, match_to):
                result += 1
        
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()