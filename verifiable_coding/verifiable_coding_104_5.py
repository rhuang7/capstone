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
        
        # Convert p to 0-based index
        p = [x-1 for x in p]
        
        # For each color, track the nodes with that color
        color_nodes = defaultdict(list)
        for i in range(n):
            color_nodes[c[i]].append(i)
        
        # For each color, find the cycles and their lengths
        # We need to find the minimal k such that there exists a cycle where all nodes in the cycle have the same color
        # And the cycle length divides k
        # So for each color, find the minimal cycle length
        min_k = float('inf')
        
        for color in color_nodes:
            nodes = color_nodes[color]
            visited = [False] * n
            for node in nodes:
                if not visited[node]:
                    # Find the cycle starting at node
                    cycle = []
                    current = node
                    while not visited[current]:
                        visited[current] = True
                        cycle.append(current)
                        current = p[current]
                    # Check if all nodes in the cycle have the same color
                    valid = True
                    for nd in cycle:
                        if c[nd] != color:
                            valid = False
                            break
                    if valid:
                        # The cycle length is len(cycle)
                        min_k = min(min_k, len(cycle))
        
        results.append(str(min_k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()