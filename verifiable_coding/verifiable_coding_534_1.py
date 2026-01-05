import sys
import collections

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
        adj = collections.defaultdict(list)
        edges = []
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            idx += 2
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)
        
        # Maximum antimatching is the maximum number of edges such that no two share a common endpoint
        # This is equivalent to finding a maximum matching in the complement graph
        # However, since the complement graph is too large, we use a different approach
        
        # The maximum size of an antimatching is the maximum number of edges such that no two share a common endpoint
        # This is equivalent to finding the maximum number of edges where each edge is disjoint from the others
        # This is the same as finding a maximum matching in the original graph
        
        # We use a standard maximum matching algorithm (DFS-based)
        # We'll use a bipartite graph approach, but since the graph is not necessarily bipartite, we'll use a general approach
        
        # We'll use a standard maximum matching algorithm for general graphs
        # We'll use the standard DFS-based approach
        
        # For each vertex, we'll try to find an augmenting path
        # We'll use a visited array to track visited vertices during DFS
        
        # We'll use a dictionary to track the match for each vertex
        match_to = {}
        
        def dfs(u, visited):
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if v not in match_to or dfs(match_to[v], visited):
                        match_to[v] = u
                        return True
            return False
        
        result = 0
        for u in range(n):
            visited = [False] * n
            if dfs(u, visited):
                result += 1
        
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()