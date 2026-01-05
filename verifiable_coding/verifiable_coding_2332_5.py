import sys
import sys
from sys import stdin
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
        
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        
        # BFS to find the component containing a and b
        visited = [False] * (n + 1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp = []
        while q:
            u = q.popleft()
            comp.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Check if a and b are in the same component
        if b not in comp:
            results.append(0)
            continue
        
        # BFS to find the component containing a but not b
        visited = [False] * (n + 1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp_a = []
        while q:
            u = q.popleft()
            comp_a.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # BFS to find the component containing b but not a
        visited = [False] * (n + 1)
        q = deque()
        q.append(b)
        visited[b] = True
        comp_b = []
        while q:
            u = q.popleft()
            comp_b.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Count the number of cities in comp_a excluding a and b
        count_a = len(comp_a) - 2
        # Count the number of cities in comp_b excluding a and b
        count_b = len(comp_b) - 2
        
        # The number of valid pairs is count_a * count_b
        results.append(count_a * count_b)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()