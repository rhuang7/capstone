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
        
        # BFS to find the component that contains a and b
        # and the component that contains a and b when a and b are removed
        # We need to find the number of pairs (x,y) such that any path from x to y goes through a and b
        # This is equivalent to finding the number of pairs (x,y) where x is in the component of a when b is removed
        # and y is in the component of b when a is removed
        
        # First, find the component of a and b
        visited = [False] * (n+1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp_ab = []
        while q:
            u = q.popleft()
            comp_ab.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Now, remove a and b and find the component of a and b
        # We need to find the component of a when b is removed
        # and the component of b when a is removed
        # We can do this by running BFS twice
        
        # Find the component of a when b is removed
        visited = [False] * (n+1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp_a_without_b = []
        while q:
            u = q.popleft()
            comp_a_without_b.append(u)
            for v in adj[u]:
                if not visited[v] and v != b:
                    visited[v] = True
                    q.append(v)
        
        # Find the component of b when a is removed
        visited = [False] * (n+1)
        q = deque()
        q.append(b)
        visited[b] = True
        comp_b_without_a = []
        while q:
            u = q.popleft()
            comp_b_without_a.append(u)
            for v in adj[u]:
                if not visited[v] and v != a:
                    visited[v] = True
                    q.append(v)
        
        # The number of pairs is the product of the sizes of the two components
        count_a = len(comp_a_without_b)
        count_b = len(comp_b_without_a)
        results.append(count_a * count_b)
    
    for res in results:
        print(res)