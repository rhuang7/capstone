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
            s = set(data[idx:idx+vi])
            idx += vi
            sets.append(s)
        # Build the bipartite graph
        # Each element is a node on the left
        # Each set is a node on the right
        # An edge exists between an element and a set if the element is in the set
        # We need to find the minimum vertex cover of this bipartite graph
        # The minimum vertex cover is equal to the maximum matching (Konig's theorem)
        # So we need to find the maximum matching
        # Then the minimum number of atoms is the size of the minimum vertex cover
        # We can model this as a bipartite graph and find the maximum matching
        # We'll use a standard maximum bipartite matching algorithm
        # Create a bipartite graph
        # Left nodes are elements 0..n-1
        # Right nodes are sets 0..m-1
        # Create adjacency list for the bipartite graph
        graph = [[] for _ in range(n)]
        for s in range(m):
            for x in sets[s]:
                graph[x].append(s)
        # Find maximum matching
        # Use standard DFS-based algorithm
        match_to = [-1] * m
        def dfs(u, visited):
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    if match_to[v] == -1 or dfs(match_to[v], visited):
                        match_to[v] = u
                        return True
            return False
        result = 0
        for u in range(n):
            visited = [False] * m
            if dfs(u, visited):
                result += 1
        results.append(result)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()