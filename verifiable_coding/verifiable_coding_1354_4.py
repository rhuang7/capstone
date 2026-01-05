import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        edges = []
        for _ in range(n-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Perform BFS to find the number of connected components
        visited = [False] * n
        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                queue = [i]
                visited[i] = True
                while queue:
                    node = queue.pop(0)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        # If there is only one component, the answer is k * (k-1)^(c-1)
        # where c is the number of components
        # But if k == 1, the answer is 1
        if k == 1:
            results.append(1)
        else:
            res = pow(k, components, MOD)
            res = res * pow(k-1, components-1, MOD) % MOD
            results.append(res)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    solve()