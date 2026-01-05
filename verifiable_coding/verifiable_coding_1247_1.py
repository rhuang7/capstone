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
        
        # Create a mapping from value to index
        value_to_index = {val: i for i, val in enumerate(P)}
        
        # Create a list of positions for each value in sorted order
        sorted_values = list(range(1, N+1))
        pos = [0] * (N+1)
        for i in range(N):
            pos[P[i]] = i
        
        # Build graph of allowed swaps
        graph = defaultdict(list)
        for i in range(1, N+1):
            j = i + D
            if j <= N:
                graph[i].append(j)
                graph[j].append(i)
        
        # BFS to find cycles and count swaps
        visited = [False] * (N+1)
        swap_count = 0
        
        for i in range(1, N+1):
            if not visited[i]:
                # Start BFS
                queue = deque()
                queue.append(i)
                visited[i] = True
                cycle = []
                while queue:
                    node = queue.popleft()
                    cycle.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Check if the cycle is correct
                if len(cycle) == 0:
                    continue
                # Check if the cycle is in the correct order
                correct_cycle = []
                for val in sorted_values:
                    correct_cycle.append(val)
                
                # Check if the cycle matches the correct cycle
                correct_cycle_indices = [pos[val] for val in correct_cycle]
                cycle_indices = [pos[val] for val in cycle]
                
                if correct_cycle_indices != cycle_indices:
                    results.append("-1")
                    break
                else:
                    # Number of swaps needed is (cycle length - 1)
                    swap_count += len(cycle) - 1
        
        results.append(str(swap_count))
    
    print("\n".join(results))