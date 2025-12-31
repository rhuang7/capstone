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
        # We'll use BFS for each node, but with some optimizations
        # However, with N up to 2e5, we need a better approach
        
        # Since the cost function is |v_y - v_x| + y - x, we can note that:
        # f(x, y) = |v_y - v_x| + (y - x)
        # This can be rewritten as (v_y - v_x) + (y - x) if v_y >= v_x, or (v_x - v_y) + (y - x) otherwise
        # Which simplifies to (v_y + y) - (v_x + x) if v_y >= v_x, or (v_x + x) - (v_y + y) otherwise
        # So f(x, y) = max(v_y + y, v_x + x) - min(v_y + y, v_x + x)
        
        # This suggests that the cost from x to y is determined by the values of v_i + i
        # So we can precompute for each node, the values of v_i + i
        
        # Let's precompute v_i + i for all i
        s = [v[i] + (i + 1) for i in range(N)]
        
        # For each query (x, y), the minimum cost is the absolute difference between s[x-1] and s[y-1]
        # Because the direct path from x to y has cost |s[y-1] - s[x-1]|
        # And any other path will have a higher or equal cost
        
        # The maximum length of a path with this cost is the number of nodes in the longest path from x to y
        # Which is the number of nodes in the path that goes through the nodes in order of increasing s[i]
        
        # So for each query, we can:
        # 1. Compute the minimum cost as abs(s[x-1] - s[y-1])
        # 2. Find the longest path from x to y with this cost
        
        # To find the longest path, we can use a BFS approach that tracks the length of the path
        
        for __ in range(Q):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            
            if x == y:
                results.append(f"{0} 1")
                continue
            
            min_cost = abs(s[x] - s[y])
            
            # Find the longest path from x to y with cost min_cost
            # We can use BFS to find the longest path with the given cost
            
            # We'll use a BFS that tracks the current node and the current cost
            # But since the cost is fixed, we can use a BFS that only allows paths with the correct cost
            
            # However, for large N, this approach may not be efficient enough
            # So we need a better way
            
            # We can use a BFS that tracks the current node and the current cost, and only explores nodes that can contribute to the path with the correct cost
            
            # We'll use a queue for BFS, and a visited array to track the maximum length for each node
            
            visited = [-1] * N
            q = deque()
            q.append(x)
            visited[x] = 1
            
            while q:
                u = q.popleft()
                for v in range(N):
                    if u == v:
                        continue
                    cost = abs(s[u] - s[v])
                    if cost == min_cost:
                        if visited[v] == -1 or visited[v] < visited[u] + 1:
                            visited[v] = visited[u] + 1
                            q.append(v)
            
            max_length = visited[y]
            results.append(f"{min_cost} {max_length}")
    
    print('\n'.join(results))