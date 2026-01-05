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
        
        # BFS to find the component that contains a and b
        # and the component that contains a but not b
        # and the component that contains b but not a
        # and the component that contains neither a nor b
        
        # First, find the component that contains a and b
        # and the component that contains a but not b
        # and the component that contains b but not a
        # and the component that contains neither a nor b
        
        # We need to find the size of the component that contains a and b
        # and the size of the component that contains a but not b
        # and the size of the component that contains b but not a
        # and the size of the component that contains neither a nor b
        
        # We can do this with BFS or DFS
        
        # Find the component that contains a and b
        visited = [False] * (n + 1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp_ab = 0
        comp_a_not_b = 0
        comp_b_not_a = 0
        comp_neither = 0
        
        while q:
            u = q.popleft()
            comp_ab += 1
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Now find the component that contains a but not b
        visited = [False] * (n + 1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp_a_not_b = 0
        while q:
            u = q.popleft()
            comp_a_not_b += 1
            for v in graph[u]:
                if not visited[v] and v != b:
                    visited[v] = True
                    q.append(v)
        
        # Now find the component that contains b but not a
        visited = [False] * (n + 1)
        q = deque()
        q.append(b)
        visited[b] = True
        comp_b_not_a = 0
        while q:
            u = q.popleft()
            comp_b_not_a += 1
            for v in graph[u]:
                if not visited[v] and v != a:
                    visited[v] = True
                    q.append(v)
        
        # Now find the component that contains neither a nor b
        visited = [False] * (n + 1)
        q = deque()
        for i in range(1, n + 1):
            if not visited[i] and i != a and i != b:
                q.append(i)
                visited[i] = True
                comp_neither = 0
                while q:
                    u = q.popleft()
                    comp_neither += 1
                    for v in graph[u]:
                        if not visited[v] and v != a and v != b:
                            visited[v] = True
                            q.append(v)
                            break
        
        # The number of pairs (x, y) such that any path from x to y goes through a and b
        # is equal to the product of the sizes of the component that contains a but not b
        # and the component that contains b but not a
        res = comp_a_not_b * comp_b_not_a
        results.append(res)
    
    for res in results:
        print(res)