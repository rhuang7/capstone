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
            color_to_nodes[c[i]].append(i + 1)  # 1-based indexing
        
        min_k = float('inf')
        
        for color in color_to_nodes:
            nodes = color_to_nodes[color]
            visited = [False] * (n + 1)
            queue = deque()
            
            for node in nodes:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    cycle = []
                    while queue:
                        current = queue.popleft()
                        if visited[current]:
                            continue
                        visited[current] = True
                        cycle.append(current)
                        next_node = p[current - 1]  # p is 0-based
                        if not visited[next_node]:
                            queue.append(next_node)
                        else:
                            if next_node in cycle:
                                idx_cycle = cycle.index(next_node)
                                cycle = cycle[idx_cycle:]
                                break
                    if len(cycle) > 1:
                        length = len(cycle)
                        k = math.lcm(*[length // gcd(length, i) for i in range(1, length)])
                        min_k = min(min_k, k)
        
        results.append(str(min_k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()