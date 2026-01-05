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
        
        # Build color to nodes map
        color_nodes = defaultdict(list)
        for i in range(n):
            color_nodes[c[i]].append(i + 1)  # 1-based index
        
        # For each color, check if there's a cycle where all nodes in the cycle have the same color
        # And find the minimal k such that the permutation p^k has at least one such cycle
        # We need to find the minimal k such that there exists a cycle in p^k where all nodes in the cycle have the same color
        
        # For each color, process its nodes
        min_k = float('inf')
        for color in color_nodes:
            nodes = color_nodes[color]
            # Check if all nodes in this color form a single cycle in the permutation
            # If not, then we need to find the LCM of cycle lengths
            visited = [False] * (n + 1)
            for node in nodes:
                if not visited[node]:
                    cycle = []
                    current = node
                    while not visited[current]:
                        visited[current] = True
                        cycle.append(current)
                        current = p[current - 1]
                    # Check if all nodes in the cycle have the same color
                    if all(c[i - 1] == color for i in cycle):
                        # Compute the length of the cycle
                        cycle_len = len(cycle)
                        # Update the minimal k
                        min_k = min(min_k, cycle_len)
        
        results.append(str(min_k))
    
    print('\n'.join(results))