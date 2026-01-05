import sys
import math
from collections import deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        v = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Preprocess for each node, the minimum cost and maximum length to all other nodes
        # Using BFS for shortest paths (since the graph is complete and edge weights are not necessarily positive)
        # But since we need to find min cost and max length, we need to run Dijkstra for each node
        # However, with N up to 2e5 and Q up to 2e5, this is not feasible
        # So we need a smarter approach
        
        # We can observe that the cost function f(x, y) = |v_y - v_x| + y - x
        # Which can be rewritten as (v_y - v_x) + (y - x) if v_y >= v_x, or (v_x - v_y) + (y - x) otherwise
        # So f(x, y) = (v_y + y) - (v_x + x) if v_y >= v_x, or (v_x + x) - (v_y + y) otherwise
        # So f(x, y) = |(v_y + y) - (v_x + x)|

        # Let's define a new array: a[i] = v[i] + i
        a = [v[i] + (i + 1) for i in range(N)]
        
        # Now, the cost from x to y is |a[y] - a[x]|
        # So the minimum cost from x to y is |a[y] - a[x]|
        # The maximum length is 2 if x != y, else 1
        
        for __ in range(Q):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            
            if x == y:
                results.append("-1 2")
                continue
            
            cost = abs(a[y] - a[x])
            length = 2
            results.append(f"{cost} {length}")
    
    print("\n".join(results))