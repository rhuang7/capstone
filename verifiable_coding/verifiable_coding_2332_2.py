import sys
import sys
from collections import deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        a = int(data[idx+2])
        b = int(data[idx+3])
        idx += 4
        
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # BFS to find the component that does not contain a or b
        visited = [False] * (n+1)
        q = deque()
        q.append(a)
        visited[a] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # BFS to find the component that contains a and b
        visited2 = [False] * (n+1)
        q = deque()
        q.append(b)
        visited2[b] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited2[v]:
                    visited2[v] = True
                    q.append(v)
        
        # Count the number of cities not in the a-b component
        cnt = 0
        for i in range(1, n+1):
            if not visited2[i]:
                cnt += 1
        
        # The answer is cnt * (cnt - 1) // 2
        results.append(cnt * (cnt - 1) // 2)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')