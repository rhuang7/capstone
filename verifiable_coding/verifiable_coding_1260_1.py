import sys
import math
from collections import deque

def solve():
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
        
        # Precompute connected components
        visited = [False] * (N+1)
        components = []
        for i in range(1, N+1):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                comp = []
                while q:
                    node = q.popleft()
                    comp.append(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                components.append(comp)
        
        # Precompute component sizes and museum counts
        comp_info = []
        for comp in components:
            total_museums = sum(museums[node-1] for node in comp)
            comp_info.append((total_museums, len(comp)))
        
        # If there are not enough components for K months, output -1
        if len(components) < K:
            results.append(-1)
            continue
        
        # For each month, choose the best possible component
        total = 0
        remaining = K
        used = set()
        
        # First month: Lavanya chooses the component with maximum museums
        max_museums = -1
        best_comp = None
        for comp in components:
            if comp not in used:
                if sum(museums[node-1] for node in comp) > max_museums:
                    max_museums = sum(museums[node-1] for node in comp)
                    best_comp = comp
        total += max_museums
        used.add(tuple(best_comp))
        remaining -= 1
        
        # Remaining months: alternate between Nikhil and Lavanya
        # Nikhil chooses the component with minimum museums
        # Lavanya chooses the component with maximum museums
        while remaining > 0:
            # Nikhil's turn: choose component with minimum museums
            min_museums = float('inf')
            best_comp_nikhil = None
            for comp in components:
                if tuple(comp) not in used:
                    if sum(museums[node-1] for node in comp) < min_museums:
                        min_museums = sum(museums[node-1] for node in comp)
                        best_comp_nikhil = comp
            total += min_museums
            used.add(tuple(best_comp_nikhil))
            remaining -= 1
            
            # Lavanya's turn: choose component with maximum museums
            max_museums = -1
            best_comp_lavanya = None
            for comp in components:
                if tuple(comp) not in used:
                    if sum(museums[node-1] for node in comp) > max_museums:
                        max_museums = sum(museums[node-1] for node in comp)
                        best_comp_lavanya = comp
            total += max_museums
            used.add(tuple(best_comp_lavanya))
            remaining -= 1
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()