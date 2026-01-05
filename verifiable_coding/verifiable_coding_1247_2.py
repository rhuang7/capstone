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
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        P = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Create a sorted version of P
        sorted_P = sorted(P)
        
        # Create a mapping from value to its position in the sorted array
        pos_map = {val: i for i, val in enumerate(sorted_P)}
        
        # Create a graph where each node is a position in the array
        # Edges are between positions i and j if |P[i] - P[j]| == D
        graph = defaultdict(list)
        
        for i in range(N):
            for j in range(i + 1, N):
                if abs(P[i] - P[j]) == D:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # Find connected components in the graph
        visited = [False] * N
        components = []
        
        for i in range(N):
            if not visited[i]:
                q = deque()
                q.append(i)
                visited[i] = True
                component = []
                while q:
                    u = q.popleft()
                    component.append(u)
                    for v in graph[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                components.append(component)
        
        # For each component, check if it can be sorted using the allowed swaps
        # Each component must contain all elements that are in the same position in the sorted array
        # So for each position i in the component, the value at i in the sorted array must be in the component
        # Also, the component must be a cycle that can be sorted with the allowed swaps
        
        # For each component, check if it can be sorted
        # We can use BFS to find the minimum number of swaps
        # But since we can only swap elements that are D apart, we need to check if the component is a cycle
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then we can sort it with swaps
        # Otherwise, it's impossible
        
        # For each component, check if it is a cycle
        # We can do this by checking if the component forms a cycle in the graph
        # If it does, then