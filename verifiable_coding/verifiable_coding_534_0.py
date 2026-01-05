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
            adj[u].append(v)
            adj[v].append(u)
            edges.append((u, v))
        
        # Maximum antimatching is the maximum number of edges such that no two share a common endpoint
        # This is equivalent to finding the maximum matching in the complement graph
        # But since we need to maximize the number of edges with no shared endpoints, we can do the following:
        # For each node, we can take at most one edge incident to it
        # So the maximum size of an antimatching is the maximum number of edges such that no two share a common endpoint
        # This is equivalent to finding the maximum matching in the original graph
        # Wait, no. Wait: in an antimatching, any two edges must share a common endpoint. So the maximum antimatching is the maximum set of edges where every pair shares a common endpoint.
        # This is equivalent to finding the maximum number of edges that form a clique in the intersection graph of edges.
        # But this is computationally expensive. However, there's a key observation:
        # The maximum size of an antimatching is equal to the maximum number of edges that can be selected such that no two share a common endpoint. Wait, no! That's the opposite.
        # Wait, no. An antimatching is a set of edges where every pair shares a common endpoint. So, for example, if you have three edges that all share a common vertex, then they form an antimatching.
        # The maximum size of an antimatching is the maximum number of edges that can be selected such that every pair of edges shares a common endpoint.
        # This is equivalent to finding the maximum number of edges that can be selected such that they all share a common vertex.
        # So the maximum size of an antimatching is the maximum degree of any vertex in the graph.
        # Because if a vertex has degree d, then you can select d edges incident to it, and all of them share that vertex, so they form an antimatching.
        # Therefore, the answer is the maximum degree of any vertex in the graph.
        
        max_degree = 0
        for u in adj:
            max_degree = max(max_degree, len(adj[u]))
        results.append(str(max_degree))
    
    print('\n'.join(results))