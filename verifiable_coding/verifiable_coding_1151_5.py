import sys
import sys
from sys import stdin
from collections import defaultdict, deque

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
        adj = defaultdict(list)
        for _ in range(M):
            a = int(data[idx])
            b = int(data[idx+1])
            adj[a].append(b)
            adj[b].append(a)
            idx += 2
        
        visited = [False] * N
        count = 0
        
        for i in range(N):
            if not visited[i]:
                queue = deque()
                queue.append(i)
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                count += 1
        
        results.append(str(count))
    
    print('\n'.join(results)) 

if __name__ == '__main__':
    solve()