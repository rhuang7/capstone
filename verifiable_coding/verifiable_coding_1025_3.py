import sys
import sys
from sys import stdin
import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Build tree and compute depths and parents for LCA
        parent = [0]*(N+1)
        depth = [0]*(N+1)
        visited = [False]*(N+1)
        stack = [(1, 0)]
        visited[1] = True
        while stack:
            node, p = stack.pop()
            parent[node] = p
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[node] + 1
                    stack.append((neighbor, node))
        
        # For each query, find all nodes in the subtree of V at even distance
        # We can do this with BFS
        # But for efficiency, we need to precompute for each node its subtree
        # and track distances
        # However, for large N and Q, this is not feasible
        # So we use a BFS for each query
        
        # We need to process queries
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        # Process queries
        for V in queries:
            # BFS from V to find all nodes in its subtree at even distance
            # (excluding V itself)
            visited_bfs = [False]*(N+1)
            queue = [(V, 0)]
            visited_bfs[V] = True
            total = 0
            while queue:
                node, dist = queue.pop(0)
                if dist % 2 == 0 and node != V:
                    total += A[node-1]
                    A[node-1] = 0
                for neighbor in adj[node]:
                    if not visited_bfs[neighbor] and parent[neighbor] == node:
                        visited_bfs[neighbor] = True
                        queue.append((neighbor, dist + 1))
            A[V-1] += total
        
        results.append(' '.join(map(str, A)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()