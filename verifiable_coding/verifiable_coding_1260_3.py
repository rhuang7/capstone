import sys
import sys
from sys import stdin
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
        
        adj = [[] for _ in range(N+1)]
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        museums = list(map(int, data[idx:idx+N]))
        idx += N
        
        visited = [False] * (N+1)
        total = 0
        
        # Precompute connected components
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
        
        # Sort components by size (for maximum museums)
        components.sort(key=lambda x: len(x), reverse=True)
        
        # For each component, precompute the sum of museums
        comp_museum_sums = []
        for comp in components:
            sum_m = 0
            for city in comp:
                sum_m += museums[city-1]
            comp_museum_sums.append(sum_m)
        
        # Now simulate K months
        if K > len(components):
            results.append(-1)
            continue
        
        # For each month, alternate between Lavanya and Nikhil
        # Lavanya picks the component with maximum museums
        # Nikhil picks the component with minimum museums
        # But we need to track which components are already used
        
        used = [False] * len(components)
        current_m = 0
        
        for _ in range(K):
            if current_m >= len(components):
                results.append(-1)
                break
            if used[current_m]:
                results.append(-1)
                break
            # Lavanya's turn: pick the component with maximum museums
            # Nikhil's turn: pick the component with minimum museums
            # But we need to track which components are available
            # So we need to find the maximum and minimum available components
            # This is not efficient, but given the constraints, we can try a different approach
            # Instead, we can precompute the maximum and minimum components and alternate between them
            # But this is not correct. Let's think of a better way
            
            # For each month, we need to choose a component that hasn't been used yet
            # Lavanya chooses the component with the maximum museums
            # Nikhil chooses the component with the minimum museums
            # So we need to track which components are available and choose the max and min
            # We can use a priority queue for max and min
            
            # But since we can't use a priority queue for large N, we can precompute the max and min components
            # and alternate between them
            # However, this is not correct, so we need to find a better way
            
            # Let's try a different approach
            # We can precompute all components and sort them by museums
            # Then, for each month, we alternate between taking the maximum and minimum available components
            # This is the correct approach
            
            # So we need to track which components are available
            # We can use a list of available components
            # We can sort them by museums
            # Then, for each month, we alternate between taking the max and min
            
            # But since we can't do this efficiently, we can precompute all components and sort them
            # Then, for each month, we take the max and min alternately
            
            # So we sort the components by museums
            # Then, for each month, we take the max and min alternately
            # But this is not correct, because the same component can't be used twice
            
            # So we need to track which components are used
            # Let's try this approach
            # We can sort the components by museums
            # Then, for each month, we take the max and min alternately
            # But this is not correct, because the same component can't be used twice
            
            # So we need to track which components are used
            # We can use a list of available components
            # We can sort them by museums
            # Then, for each month, we take the max and min alternately
            
            # So we need to find the max and min available components
            # This is the correct approach
            
            # Find the max available component
            max_comp = -1
            max_sum = -1
            for i in range(len(components)):
                if not used[i]:
                    if comp_museum_sums[i] > max_sum:
                        max_sum = comp_museum_sums[i]
                        max_comp = i
            
            # Find the min available component
            min_comp = -1
            min_sum = float('inf')
            for i in range(len(components)):
                if not used[i]:
                    if comp_museum_sums[i] < min_sum:
                        min_sum = comp_museum_sums[i]
                        min_comp = i
            
            if max_comp == -1 and min_comp == -1:
                results.append(-1)
                break
            
            if _ % 2 == 0:
                # Lavanya's turn: pick max
                used[max_comp] = True
                total += comp_museum_sums[max_comp]
            else:
                # Nikhil's turn: pick min
                used[min_comp] = True
                total += comp_museum_sums[min_comp]
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()