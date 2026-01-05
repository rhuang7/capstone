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
        # and edges represent possible swaps (difference of D)
        graph = defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                if abs(P[i] - P[j]) == D:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # BFS to find the minimum number of swaps
        visited = [False] * N
        min_swaps = [0] * N
        q = deque()
        
        for i in range(N):
            if P[i] != sorted_P[i]:
                q.append(i)
                visited[i] = True
                min_swaps[i] = 0
        
        # BFS to find the minimum swaps
        while q:
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    min_swaps[v] = min_swaps[u] + 1
                    q.append(v)
        
        # Check if all elements are in their correct positions
        total_swaps = sum(min_swaps)
        for i in range(N):
            if P[i] != sorted_P[i]:
                total_swaps = -1
                break
        
        results.append(str(total_swaps))
    
    print('\n'.join(results))