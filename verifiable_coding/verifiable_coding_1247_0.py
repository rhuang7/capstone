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
        pos = {val: i for i, val in enumerate(sorted_P)}
        
        # Create a graph where each node is a position in the original array
        # and edges represent valid swaps (difference of D)
        graph = defaultdict(list)
        for i in range(N):
            for j in range(i + 1, N):
                if abs(P[i] - P[j]) == D:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # BFS to find the minimum number of swaps to sort the array
        # We need to find the minimum number of swaps to bring each element to its correct position
        # We can model this as a graph where each node is a position, and edges are valid swaps
        # We need to find the minimum number of swaps to reach the correct position for each element
        
        # Create a list to store the number of swaps needed for each position
        swaps = [0] * N
        
        # For each position, if it's not already correct, perform BFS to find the minimum swaps
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                # Start BFS from position i
                queue = deque()
                queue.append((i, 0))
                visited[i] = True
                while queue:
                    node, count = queue.popleft()
                    # Check if this node is already in the correct position
                    if P[node] == sorted_P[node]:
                        continue
                    # Check if this node is in the correct position in the sorted array
                    correct_pos = pos[P[node]]
                    if correct_pos == node:
                        continue
                    # If not, check if we can swap with another node
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append((neighbor, count + 1))
                            swaps[neighbor] = count + 1
                    # If we can't reach the correct position, it's impossible
                    if not queue:
                        results.append(-1)
                        break
                else:
                    # If we successfully reached the correct positions, sum the swaps
                    total = sum(swaps)
                    results.append(total)
        # If any test case is impossible, return -1
        if -1 in results:
            results = [-1]
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()