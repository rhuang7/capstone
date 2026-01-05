import sys
import math
from collections import defaultdict, deque

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
        
        adj = defaultdict(list)
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        museums = list(map(int, data[idx:idx+N]))
        idx += N
        
        visited = [False] * (N + 1)
        total = 0
        
        # Precompute connected components
        components = []
        for i in range(1, N + 1):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                comp = []
                while q:
                    u = q.popleft()
                    comp.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                components.append(comp)
        
        # Sort components by size (largest first)
        components.sort(key=lambda x: len(x), reverse=True)
        
        # For each component, precompute the sum of museums
        comp_museum_sums = []
        for comp in components:
            s = 0
            for city in comp:
                s += museums[city - 1]
            comp_museum_sums.append(s)
        
        # If there are not enough components for K months, output -1
        if len(components) < K:
            results.append("-1")
            continue
        
        # Simulate K months
        for i in range(K):
            if i % 2 == 0:
                # Lavanya's turn: choose the component with maximum museums
                if not comp_museum_sums:
                    results.append("-1")
                    break
                total += comp_museum_sums[0]
                comp_museum_sums.pop(0)
            else:
                # Nikhil's turn: choose the component with minimum museums
                if not comp_museum_sums:
                    results.append("-1")
                    break
                total += comp_museum_sums[-1]
                comp_museum_sums.pop()
        
        results.append(str(total))
    
    for res in results:
        print(res)