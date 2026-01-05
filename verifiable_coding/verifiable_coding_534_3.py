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
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Maximum antimatching is the maximum number of edges such that no two share a vertex
        # This is equivalent to finding a maximum matching in the complement graph
        # But since the complement graph is too large, we use a different approach
        
        # The maximum antimatching is the maximum number of edges that form a matching in the original graph
        # Wait, no. The antimatching requires that every pair of edges shares a vertex, which is the opposite of a matching
        # So the maximum antimatching is the maximum number of edges such that every pair shares a vertex
        
        # This is equivalent to finding the maximum number of edges that can be selected such that they all share at least one common vertex
        # So the maximum antimatching is the maximum degree of any vertex in the graph
        
        max_degree = 0
        for u in adj:
            max_degree = max(max_degree, len(adj[u]))
        results.append(str(max_degree))
    
    print('\n'.join(results))