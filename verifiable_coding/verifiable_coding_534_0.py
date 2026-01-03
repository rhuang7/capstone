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
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        graph = defaultdict(list)
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            graph[u].append(v)
            graph[v].append(u)
            idx += 2
        
        # Maximum antimatching is the maximum number of edges such that no two share a common endpoint
        # This is equivalent to finding a maximum matching in the line graph of the original graph
        # But since the line graph is complex, we can use a greedy approach here
        
        # We can use a greedy algorithm: for each node, if it is not yet matched, we try to match it with an adjacent node
        # We'll track which nodes are used
        used = [False] * n
        count = 0
        
        for u in range(n):
            if not used[u]:
                for v in graph[u]:
                    if not used[v]:
                        used[u] = True
                        used[v] = True
                        count += 1
                        break
        
        results.append(str(count))
    
    print('\n'.join(results))