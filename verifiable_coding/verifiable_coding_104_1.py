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
        p = list(map(int, data[idx:idx+n]))
        idx += n
        c = list(map(int, data[idx:idx+n]))
        idx += n
        
        color_to_nodes = defaultdict(list)
        for i in range(n):
            color_to_nodes[c[i]].append(i)
        
        visited = [False] * n
        min_k = float('inf')
        
        for color in color_to_nodes:
            nodes = color_to_nodes[color]
            for i in nodes:
                if visited[i]:
                    continue
                q = deque()
                q.append(i)
                visited[i] = True
                cycle = []
                while q:
                    u = q.popleft()
                    cycle.append(u)
                    next_u = p[u] - 1
                    if visited[next_u]:
                        if c[next_u] == color:
                            cycle.append(next_u)
                            break
                        else:
                            break
                    visited[next_u] = True
                    q.append(next_u)
                
                if len(cycle) >= 2:
                    l = len(cycle)
                    g = math.gcd(l, len(cycle))
                    k = l // g
                    if k < min_k:
                        min_k = k
        
        results.append(str(min_k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()