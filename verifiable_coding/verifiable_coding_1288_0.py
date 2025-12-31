import sys
import math
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
        idx += 2
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            u = int(data[idx])
            v = int(data[idx+1])
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        
        visited = [False] * (N+1)
        count = 0
        
        for i in range(1, N+1):
            if not visited[i]:
                count += 1
                queue = deque()
                queue.append(i)
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()