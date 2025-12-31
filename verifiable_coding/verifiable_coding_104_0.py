import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
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
            color_to_nodes[c[i]].append(i + 1)  # 1-based index
        
        min_k = float('inf')
        
        for color in color_to_nodes:
            nodes = color_to_nodes[color]
            visited = [False] * (n + 1)
            for node in nodes:
                if not visited[node]:
                    queue = deque()
                    queue.append(node)
                    visited[node] = True
                    cycle = []
                    while queue:
                        current = queue.popleft()
                        cycle.append(current)
                        next_node = p[current - 1]  # p is 0-based
                        if visited[next_node]:
                            if next_node in cycle:
                                idx_cycle = cycle.index(next_node)
                                cycle = cycle[idx_cycle:]
                                break
                        else:
                            visited[next_node] = True
                            queue.append(next_node)
                    if len(cycle) > 1:
                        length = len(cycle)
                        k = math.lcm(*[length // g for g in set(math.gcd(length, i) for i in range(1, length))])
                        min_k = min(min_k, k)
        
        results.append(str(min_k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()