import sys
import math
from collections import deque, defaultdict

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
        
        adj = [[] for _ in range(N+1)]
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        museums = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute connected components
        visited = [False] * (N + 1)
        components = []
        for i in range(1, N+1):
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
        
        # For each component, sort by museum count (for Lavanya to choose max)
        comp_museum_sum = []
        for comp in components:
            total = sum(museums[u-1] for u in comp)
            comp_museum_sum.append(total)
        
        # Sort components by museum count (for Lavanya to choose max)
        comp_museum_sum.sort(reverse=True)
        
        # If K exceeds the number of components, output -1
        if K > len(comp_museum_sum):
            results.append("-1")
            continue
        
        # Lavanya and Nikhil alternate turns
        # Lavanya starts first, chooses the component with max museums
        # Nikhil chooses the next component with max museums (but not chosen)
        # We need to simulate K months
        
        # We will use a priority queue to select the next component
        # But since the components are already sorted, we can just take the first K components
        # But we need to alternate between Lavanya and Nikhil
        
        # We need to simulate the selection of components for K months
        # Lavanya picks the component with max museums (not yet picked)
        # Nikhil picks the component with max museums (not yet picked)
        # But since the components are already sorted, we can simulate this
        
        # We will use a list to track which components are picked
        picked = [False] * len(comp_museum_sum)
        total = 0
        
        for month in range(K):
            if picked[0]:
                # Nikhil's turn, pick the next component with max museums
                for i in range(len(comp_museum_sum)):
                    if not picked[i]:
                        total += comp_museum_sum[i]
                        picked[i] = True
                        break
            else:
                # Lavanya's turn, pick the component with max museums
                for i in range(len(comp_museum_sum)):
                    if not picked[i]:
                        total += comp_museum_sum[i]
                        picked[i] = True
                        break
        
        results.append(str(total))
    
    for res in results:
        print(res)