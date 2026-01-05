import sys
import math
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
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Build the BFS order and track the level of each node
        level = [0] * (n + 1)
        q = deque()
        q.append(1)
        level[1] = 0
        current_level = 0
        next_level = 0
        
        while q:
            u = q.popleft()
            for v in a:
                if level[v] == 0 and v != 1:
                    level[v] = level[u] + 1
                    q.append(v)
                    next_level += 1
            current_level = next_level
            next_level = 0
        
        max_level = max(level[1:])
        results.append(str(max_level))
    
    print('\n'.join(results))