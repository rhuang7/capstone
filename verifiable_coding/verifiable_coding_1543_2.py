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
        
        # Build the incidence matrix
        # Each element in X is in some sets
        # We need to find the minimum number of atoms
        # An atom is a subset of X such that for each Si, it is either a subset or disjoint
        # This is equivalent to finding the minimum number of elements in a partition of X such that each element is in exactly one atom and for each Si, all elements in the atom are in Si or none are
        
        # We can model this as a bipartite graph matching problem
        # Each element in X is a node on the left
        # Each set Si is a node on the right
        # An edge connects an element x to Si if x is in Si
        # We want to find the minimum number of atoms, which is the minimum number of elements that can be chosen such that each set Si has all its elements in exactly one of the atoms
        
        # This is equivalent to finding the maximum matching in the bipartite graph
        # The minimum number of atoms is equal to the number of elements in X minus the size of the maximum matching
        
        # Build the bipartite graph
        from collections import defaultdict
        graph = defaultdict(list)
        for i in range(m):
            for x in sets[i]:
                graph[x].append(i)
        
        # Find maximum bipartite matching
        def bpm(u, visited, match_to):
            for v in graph[u]:
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
        
        results.append(n - result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()