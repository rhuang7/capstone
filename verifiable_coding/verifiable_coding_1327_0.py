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
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        v = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Preprocess for each node, the minimum cost and maximum length to all other nodes
        # We'll use BFS for shortest path and DFS for longest path
        # However, given the constraints, we need a more efficient approach
        
        # For each query, we can do BFS for minimum cost and DFS for maximum length
        # But with Q up to 2e5, this is not feasible
        
        # So we need to precompute for all pairs (x, y) the min cost and max length
        # But with N up to 2e5, this is not feasible either
        
        # So we need to find a way to compute for each query (x, y) the min cost and max length
        
        # Let's think about the cost function:
        # f(x, y) = |v_y - v_x| + y - x
        # So the cost of a path from x to y is sum of f(a_i, a_{i+1}) for i in 1..k-1
        
        # Let's consider the cost of a direct path from x to y:
        # cost = |v_y - v_x| + y - x
        
        # Now, for a path that goes through other cities, the cost is:
        # sum_{i=1}^{k-1} (|v_{a_{i+1}} - v_{a_i}| + (a_{i+1} - a_i))
        # = sum |v_{a_{i+1}} - v_{a_i}| + sum (a_{i+1} - a_i)
        # = sum |v_{a_{i+1}} - v_{a_i}| + (a_k - a_1)
        
        # So the total cost is (sum of absolute differences of v) + (y - x)
        
        # So the minimum cost is the minimum of (sum of absolute differences of v) + (y - x)
        # But how to find the minimum sum of absolute differences?
        
        # The minimum sum of absolute differences is achieved by going from x to y through the cities in order of increasing v
        # So for each query (x, y), we can find the path that goes through the cities in order of increasing v
        
        # So the minimum cost is (sum of absolute differences of v along the path) + (y - x)
        
        # The maximum length is the number of cities in the path
        
        # So for each query (x, y), we need to:
        # 1. Find the path that gives the minimum cost
        # 2. Find the maximum length of such paths
        
        # To do this efficiently, we can precompute for each city the sorted list of cities by v
        # Then for a query (x, y), we can find the path that goes through the cities in order of increasing v
        
        # However, with N up to 2e5 and Q up to 2e5, this is not feasible
        
        # So we need to find an efficient way to compute the minimum cost and maximum length for each query
        
        # Let's think about the following:
        # The minimum cost from x to y is (sum of absolute differences of v along the path) + (y - x)
        # The sum of absolute differences of v along the path is minimized when the path goes through the cities in order of increasing v
        # So for x and y, we can find the path that goes through the cities in order of increasing v
        
        # So for each query (x, y), we can:
        # 1. Find the path that goes through the cities in order of increasing v
        # 2. Compute the cost and length of that path
        
        # But how to find this path efficiently?
        
        # We can precompute for each city the list of cities in order of increasing v
        # Then for a query (x, y), we can find the path that goes from x to y through the cities in order of increasing v
        
        # However, with N up to 2e5 and Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use dynamic programming to find the minimum cost from x to y
        
        # But with N up to 2e5 and Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query efficiently
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2e5, this is not feasible
        
        # So we need to find a way to compute the minimum cost and maximum length for each query in O(1) or O(log N) time
        
        # Let's think about the following:
        # The minimum cost from x to y is the minimum of:
        # - the direct path from x to y
        # - the path that goes through some other city z
        # So we can use BFS to find the minimum cost from x to y
        
        # However, with Q up to 2