import sys
import math
from collections import deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        
        edges = []
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            edges.append((u, v))
            idx += 2
        
        museums = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Build adjacency list
        adj = [[] for _ in range(N+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Find connected components
        visited = [False] * (N+1)
        components = []
        for i in range(1, N+1):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                component = []
                while q:
                    node = q.popleft()
                    component.append(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                components.append(component)
        
        # Precompute component sizes and museum counts
        comp_info = []
        for comp in components:
            total_museums = sum(museums[node-1] for node in comp)
            comp_info.append((total_museums, len(comp)))
        
        # Sort components by museum count (for Lavanya's choice)
        comp_info.sort(reverse=True)
        
        # If K exceeds the number of components, output -1
        if K > len(comp_info):
            results.append("-1")
            continue
        
        # Simulate K months
        total = 0
        remaining = K
        used = set()
        
        # Lavanya starts first
        turn = 0  # 0 for Lavanya, 1 for Nikhil
        
        for i in range(len(comp_info)):
            if remaining == 0:
                break
            if turn == 0:
                # Lavanya chooses the component with max museums
                total += comp_info[i][0]
                used.update(comp_info[i][1])
                turn = 1
            else:
                # Nikhil chooses the component with min museums
                total += comp_info[i][0]
                used.update(comp_info[i][1])
                turn = 0
            remaining -= 1
        
        results.append(str(total))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()