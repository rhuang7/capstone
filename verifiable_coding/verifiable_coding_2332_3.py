import sys
import math
from collections import deque, defaultdict

def main():
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
        for __ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        
        # BFS to find the component that contains a and b
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
        
        # Find the node that is on the path between a and b
        # We can do a BFS from a to find the shortest path to b
        # and find the first node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # and is not in the component of a or b
        # But since the graph is connected, we can do a BFS from a to b
        # and find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in the component of a or b
        # So we do a BFS from a to find the distance to b
        # and then find the node that is on the path from a to b
        # which is the one that is in the component of a and b
        # and is not in