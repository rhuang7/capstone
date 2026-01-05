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
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        c = list(map(int, data[idx:idx + n]))
        idx += n
        
        color_to_nodes = defaultdict(list)
        for i in range(n):
            color_to_nodes[c[i]].append(i + 1)  # 1-based
        
        min_k = float('inf')
        
        for color in color_to_nodes:
            nodes = color_to_nodes[color]
            visited = [False] * (n + 1)
            queue = deque()
            for node in nodes:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    while queue:
                        u = queue.popleft()
                        for v in p[u - 1] - 1:
                            if not visited[v]:
                                visited[v] = True
                                queue.append(v)
            for i in range(n):
                if not visited[i + 1]:
                    continue
                cycle = []
                current = i + 1
                while True:
                    cycle.append(current)
                    current = p[current - 1]
                    if current in cycle:
                        break
                length = len(cycle)
                if length == 1:
                    min_k = 1
                    break
                for d in range(1, length):
                    if all(c[i] == c[j] for i, j in zip(cycle, cycle[d:])):
                        min_k = min(min_k, d)
                        break
                if min_k == 1:
                    break
            if min_k == 1:
                break
        
        results.append(str(min_k))
    
    print('\n'.join(results))