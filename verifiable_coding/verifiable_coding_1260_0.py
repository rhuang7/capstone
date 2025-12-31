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
        
        roads = []
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            roads.append((u, v))
            idx += 2
        
        museums = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Build graph
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        # Precompute connected components
        visited = [False] * (N + 1)
        components = []
        for i in range(1, N + 1):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                comp = []
                while q:
                    node = q.popleft()
                    comp.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                components.append(comp)
        
        # Precompute component sizes and museum counts
        comp_info = []
        for comp in components:
            comp_museums = sum(museums[node - 1] for node in comp)
            comp_size = len(comp)
            comp_info.append((comp_museums, comp_size))
        
        # If K is larger than number of components, output -1
        if K > len(components):
            results.append("-1")
            continue
        
        # Initialize variables
        total = 0
        visited_cities = set()
        remaining_months = K
        current_component = 0
        
        # First month: Lavanya chooses the component with maximum museums
        max_museums = -1
        best_component = 0
        for i in range(len(comp_info)):
            if comp_info[i][0] > max_museums:
                max_museums = comp_info[i][0]
                best_component = i
        
        # Add the best component
        total += max_museums
        visited_cities.update(components[best_component])
        remaining_months -= 1
        current_component = best_component
        
        # Remaining months: alternate between Nikhil and Lavanya
        # Nikhil chooses the component with minimum museums
        # Lavanya chooses the component with maximum museums
        while remaining_months > 0:
            # Nikhil's turn: choose component with minimum museums
            min_museums = float('inf')
            best_nikhil = -1
            for i in range(len(comp_info)):
                if i not in visited_cities:
                    if comp_info[i][0] < min_museums:
                        min_museums = comp_info[i][0]
                        best_nikhil = i
            
            if best_nikhil == -1:
                # No unvisited components
                results.append("-1")
                break
            
            total += min_museums
            visited_cities.update(components[best_nikhil])
            remaining_months -= 1
            current_component = best_nikhil
        
        # If we have completed all months
        if remaining_months == 0:
            results.append(str(total))
        else:
            results.append("-1")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()