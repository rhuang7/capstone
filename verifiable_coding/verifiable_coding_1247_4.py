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
        
        # Create a sorted version of the permutation
        sorted_P = sorted(P)
        
        # Create a mapping from value to its position in the sorted array
        pos = {val: i for i, val in enumerate(sorted_P)}
        
        # Create a graph where each node is a position in the permutation
        # and edges represent valid swaps (difference of D)
        graph = defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                if abs(P[i] - P[j]) == D:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # Find connected components in the graph
        visited = [False] * N
        components = []
        for i in range(N):
            if not visited[i]:
                component = []
                queue = deque([i])
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    component.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                components.append(component)
        
        # For each component, check if it can be sorted with swaps
        # Each component must contain all elements in the sorted array that are in the same connected component
        # We can use BFS to find the minimum number of swaps
        # Each swap can fix two elements, so the number of swaps is (size of component - number of cycles) // 2
        total_swaps = 0
        for comp in components:
            # Get the values in this component
            values = [P[i] for i in comp]
            # Get the positions of these values in the sorted array
            sorted_positions = [pos[val] for val in values]
            # Check if the sorted positions form a cycle
            # If not, it's impossible to sort
            visited_pos = [False] * N
            cycles = 0
            for i in range(len(sorted_positions)):
                if not visited_pos[i]:
                    cycle = 0
                    j = i
                    while not visited_pos[j]:
                        visited_pos[j] = True
                        j = sorted_positions[j]
                        cycle += 1
                    if cycle > 1:
                        cycles += 1
            # The number of swaps needed for this component is (size of component - number of cycles) // 2
            # But we need to ensure that the component contains all the elements in the sorted array
            # So we need to check if the component has all the elements in the sorted array
            # We can do this by checking if the set of values in the component is the same as the set of values in the sorted array
            # But since it's a permutation, it's guaranteed to have all elements
            # So we can proceed
            total_swaps += (len(comp) - cycles) // 2
        
        results.append(total_swaps)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()