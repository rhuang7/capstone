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
        
        graph = defaultdict(list)
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
        
        # Find the node that is the only common node between the two BFS traversals
        # First BFS from a
        visited_a = [False] * (n + 1)
        q = deque()
        q.append(a)
        visited_a[a] = True
        nodes_a = []
        while q:
            u = q.popleft()
            nodes_a.append(u)
            for v in graph[u]:
                if not visited_a[v]:
                    visited_a[v] = True
                    q.append(v)
        
        # Second BFS from b
        visited_b = [False] * (n + 1)
        q = deque()
        q.append(b)
        visited_b[b] = True
        nodes_b = []
        while q:
            u = q.popleft()
            nodes_b.append(u)
            for v in graph[u]:
                if not visited_b[v]:
                    visited_b[v] = True
                    q.append(v)
        
        # Find the intersection of nodes_a and nodes_b
        common = []
        for u in nodes_a:
            if u in nodes_b:
                common.append(u)
        
        # The common node is the one that is in both BFS traversals
        # It must be the only one, since a and b are in the same component
        common_node = common[0]
        
        # BFS from common_node to find the number of nodes in the component
        visited_common = [False] * (n + 1)
        q = deque()
        q.append(common_node)
        visited_common[common_node] = True
        count = 0
        while q:
            u = q.popleft()
            count += 1
            for v in graph[u]:
                if not visited_common[v]:
                    visited_common[v] = True
                    q.append(v)
        
        # The answer is (count - 2) * (count - 3) // 2
        if count < 2:
            results.append(0)
        else:
            res = (count - 2) * (count - 3) // 2
            results.append(res)
    
    for res in results:
        print(res)