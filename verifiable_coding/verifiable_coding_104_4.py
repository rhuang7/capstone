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
            color_to_nodes[c[i]].append(i + 1)  # 1-based index
        
        # For each color, find the minimum k such that there exists a cycle in p^k where all elements have the same color
        min_k = float('inf')
        
        for color, nodes in color_to_nodes.items():
            # For each node in this color, find its cycle in the permutation
            visited = [False] * (n + 1)
            for node in nodes:
                if not visited[node]:
                    cycle = []
                    current = node
                    while not visited[current]:
                        visited[current] = True
                        cycle.append(current)
                        current = p[current - 1]  # p is 1-based
                    # Check if all elements in the cycle have the same color
                    cycle_color = c[current - 1]
                    if all(c[i - 1] == cycle_color for i in cycle):
                        # Compute the length of the cycle
                        l = len(cycle)
                        # The minimum k for this cycle is the length of the cycle
                        min_k = min(min_k, l)
        
        results.append(str(min_k))
    
    print('\n'.join(results))