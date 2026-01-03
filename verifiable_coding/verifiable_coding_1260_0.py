import sys
import math
from collections import defaultdict, deque

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
        
        graph = defaultdict(list)
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        
        museums = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute connected components
        visited = [False] * (N + 1)
        components = []
        for i in range(1, N + 1):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                component = []
                while q:
                    node = q.popleft()
                    component.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                components.append(component)
        
        # Precompute component sizes and museum counts
        comp_size = []
        comp_museum = []
        for comp in components:
            size = len(comp)
            total = sum(museums[node - 1] for node in comp)
            comp_size.append(size)
            comp_museum.append(total)
        
        # If there are not enough components for K months, output -1
        if len(components) < K:
            results.append("-1")
            continue
        
        # Simulate the K months
        total_museums = 0
        visited_cities = set()
        remaining_months = K
        current_component = 0
        
        while remaining_months > 0:
            # Lavanya chooses the component with maximum museums
            max_museum = -1
            best_comp = -1
            for i in range(len(components)):
                if i not in visited_cities:
                    if comp_museum[i] > max_museum:
                        max_museum = comp_museum[i]
                        best_comp = i
            if best_comp == -1:
                # No unvisited components, break
                break
            # Add this component's museums
            total_museums += comp_museum[best_comp]
            # Mark all cities in this component as visited
            for city in components[best_comp]:
                visited_cities.add(city)
            # Remove this component from the list
            components.pop(best_comp)
            comp_size.pop(best_comp)
            comp_museum.pop(best_comp)
            remaining_months -= 1
        
        # Check if we have enough components for K months
        if len(components) < K:
            results.append("-1")
        else:
            results.append(str(total_museums))
    
    print('\n'.join(results))