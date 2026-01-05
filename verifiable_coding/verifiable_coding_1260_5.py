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
        
        visited = [False] * (N + 1)
        total = 0
        
        # Precompute connected components
        components = []
        visited_comp = [False] * (N + 1)
        for i in range(1, N+1):
            if not visited_comp[i]:
                q = deque()
                q.append(i)
                visited_comp[i] = True
                comp = []
                while q:
                    node = q.popleft()
                    comp.append(node)
                    for nei in adj[node]:
                        if not visited_comp[nei]:
                            visited_comp[nei] = True
                            q.append(nei)
                components.append(comp)
        
        # Sort components by size (for optimal selection)
        components.sort(key=lambda x: len(x), reverse=True)
        
        # Precompute component museum counts
        comp_museum = []
        for comp in components:
            sum_m = 0
            for node in comp:
                sum_m += museums[node-1]
            comp_museum.append(sum_m)
        
        # If K is larger than the number of components, output -1
        if K > len(components):
            results.append(-1)
            continue
        
        # Simulate K months
        for i in range(K):
            if i % 2 == 0:
                # Lavanya's turn: choose component with maximum museums
                if not components:
                    results.append(-1)
                    break
                comp = components[0]
                total += comp_museum[0]
                # Remove this component from the list
                components.pop(0)
                comp_museum.pop(0)
            else:
                # Nikhil's turn: choose component with minimum museums
                if not components:
                    results.append(-1)
                    break
                comp = components[-1]
                total += comp_museum[-1]
                # Remove this component from the list
                components.pop()
                comp_museum.pop()
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()