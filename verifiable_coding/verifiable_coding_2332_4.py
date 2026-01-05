import sys
import math
from collections import deque, defaultdict

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
        
        # BFS to find the component containing a and b
        visited = [False] * (n+1)
        q = deque()
        q.append(a)
        visited[a] = True
        comp = []
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Check if a and b are in the same component
        if b not in comp:
            results.append(0)
            continue
        
        # Find the node that is on the path between a and b
        # Perform BFS from a to find distances
        dist_a = [-1] * (n+1)
        q = deque()
        q.append(a)
        dist_a[a] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist_a[v] == -1:
                    dist_a[v] = dist_a[u] + 1
                    q.append(v)
        
        # Find the node with the maximum distance from a to b
        max_dist = -1
        candidate = -1
        for u in comp:
            if dist_a[u] == -1:
                continue
            if dist_a[u] + dist_a[b] == dist_a[a] + dist_a[b] - 1:
                # This node is on the path between a and b
                if dist_a[u] > max_dist:
                    max_dist = dist_a[u]
                    candidate = u
        
        # If no such node found, then a and b are not connected (but the problem says they are)
        # So we can safely assume candidate is found
        # Now find the size of the component excluding a, b, and the candidate
        # Perform BFS from candidate to find the size of the component
        visited = [False] * (n+1)
        q = deque()
        q.append(candidate)
        visited[candidate] = True
        count = 0
        while q:
            u = q.popleft()
            count += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # The number of valid pairs is (count - 2) choose 2
        if count < 2:
            results.append(0)
        else:
            res = (count - 2) * (count - 3) // 2
            results.append(res)
    
    for result in results:
        print(result)