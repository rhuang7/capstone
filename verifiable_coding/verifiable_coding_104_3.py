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
            color_nodes[c[i]].append(i + 1)  # 1-based indexing
        
        # For each color, check if there's a cycle where all nodes in the cycle have the same color
        # And find the minimum k such that p^k has an infinite path
        min_k = float('inf')
        
        for color in color_nodes:
            nodes = color_nodes[color]
            # Check if there's a cycle in the permutation where all nodes have the same color
            visited = [False] * (n + 1)
            for node in nodes:
                if not visited[node]:
                    # Find the cycle starting at node
                    cycle = []
                    current = node
                    while not visited[current]:
                        visited[current] = True
                        cycle.append(current)
                        current = p[current - 1]  # p is 1-based
                    # Check if all nodes in the cycle have the same color
                    if all(c[i - 1] == color for i in cycle):
                        # Compute the length of the cycle
                        l = len(cycle)
                        # The minimum k for this cycle is l if l is the smallest such
                        min_k = min(min_k, l)
        
        results.append(min_k)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()