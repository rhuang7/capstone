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
        # Since N is up to 2e5, we need an efficient way
        # We'll use BFS for each node, but that's O(N^2), which is too slow
        # Instead, we'll use dynamic programming based on the structure of the cost function
        
        # For each query (x, y), we need to find:
        # 1. The minimum cost from x to y
        # 2. The maximum length of a path with that cost
        
        # We'll precompute for each node, the minimum cost and max length to all other nodes
        # But for large N, this is not feasible, so we'll compute on the fly for each query
        
        # For each query, we'll perform a BFS or Dijkstra's algorithm to find the minimum cost
        # and track the maximum length for that cost
        
        # Since the cost function can be negative, we need to use Dijkstra's algorithm
        # with a priority queue
        
        # However, for large N and Q, this is O(Q*N log N), which may be too slow
        
        # So we need a smarter approach
        
        # Let's think about the cost function:
        # f(x, y) = |v_y - v_x| + (y - x)
        # So for a path from x to y, the cost is the sum of these values for each step
        
        # The minimum cost path from x to y can be found using Dijkstra's algorithm
        # But since the graph is complete, we can optimize
        
        # Let's precompute for each node, the minimum cost and max length to all other nodes
        # But for large N, this is not feasible
        
        # So we'll process each query separately, using Dijkstra's algorithm
        
        # However, for large Q and N, this may not be efficient enough
        
        # So we need to find a way to compute the minimum cost and max length for each query
        
        # Let's think about the cost function again:
        # f(x, y) = |v_y - v_x| + (y - x)
        # This can be rewritten as:
        # f(x, y) = (v_y - v_x) + (y - x) if v_y >= v_x
        #         = (v_x - v_y) + (y - x) if v_y < v_x
        # So f(x, y) = (v_y - v_x) + (y - x) if v_y >= v_x
        #         = (v_x - v_y) + (y - x) if v_y < v_x
        # Which can be written as:
        # f(x, y) = (v_y + y) - (v_x + x) if v_y >= v_x
        #         = (v_x + x) - (v_y + y) if v_y < v_x
        # So f(x, y) = |(v_y + y) - (v_x + x)|
        
        # So the cost from x to y is the absolute difference between (v_x + x) and (v_y + y)
        
        # This is a key insight! The cost of a direct path from x to y is the absolute difference between (v_x + x) and (v_y + y)
        
        # Now, the minimum cost from x to y is the minimum of all possible paths, but since the graph is complete, the minimum cost is the direct path from x to y
        
        # Wait, no. Because there might be a longer path with lower cost. For example, going through other cities might give a lower total cost
        
        # So we need to find the minimum cost path from x to y, which is not necessarily the direct path
        
        # But with the cost function being f(x, y) = |(v_y + y) - (v_x + x)|, we can model this as a graph where the edge weight is the absolute difference between (v_x + x) and (v_y + y)
        
        # So the problem reduces to finding the shortest path from x to y in a graph where the edge weight between any two nodes is the absolute difference between (v_x + x) and (v_y + y)
        
        # But this is a complete graph, so we can't use Dijkstra's algorithm directly for each query
        
        # However, we can use the fact that the cost function is the absolute difference between two values
        
        # Let's define for each node i: a_i = v_i + i
        
        # Then the cost from x to y is |a_x - a_y|
        
        # So the minimum cost from x to y is the minimum of |a_x - a_y|, |a_x - a_z| + |a_z - a_y|, etc.
        
        # But this is the same as the minimum of all possible paths, which is just |a_x - a_y|, since the triangle inequality holds
        
        # Wait, that's not correct. The triangle inequality says that |a_x - a_y| <= |a_x - a_z| + |a_z - a_y|. So the direct path is the minimum possible
        
        # So the minimum cost from x to y is |a_x - a_y|
        
        # So for any query (x, y), the minimum cost is |a_x - a_y|
        
        # Now, the maximum length of a path with this cost is the longest possible path that has this cost
        
        # So for the query (x, y), the minimum cost is |a_x - a_y|, and the maximum length is the number of nodes in the longest path that has this cost
        
        # But how to find the maximum length of a path with cost |a_x - a_y|?
        
        # The maximum length is the number of nodes in the longest path that starts at x and ends at y, and has cost |a_x - a_y|
        
        # But how to find that?
        
        # Since the cost is |a_x - a_y|, the path must have the same total cost as the direct path
        
        # This is a very difficult problem to solve for large N and Q
        
        # However, we can use the following observation:
        # The cost of a path from x to y is the sum of the costs of each edge in the path
        # And the cost of each edge is |a_i - a_j|
        
        # So the total cost of a path from x to y is the sum of |a_i - a_j| for each consecutive pair (i, j) in the path
        
        # But this is not the same as |a_x - a_y|
        
        # So the earlier conclusion that the minimum cost is |a_x - a_y| is incorrect
        
        # So we need to go back to the original problem
        
        # Let's think about the problem again
        
        # The cost of a path from x to y is the sum of f(a_i, a_{i+1}) for each step in the path
        
        # And f(a_i, a_{i+1}) = |v_{i+1} - v_i| + (i+1 - i) = |v_{i+1} - v_i| + 1
        
        # So the cost of a path is the sum of |v_{i+1} - v_i| + 1 for each step
        
        # So for a path of length k, the cost is sum_{i=1}^{k-1} (|v_{i+1} - v_i| + 1) = sum_{i=1}^{k-1} |v_{i+1} - v_i| + (k-1)
        
        # So the cost of a path is the sum of absolute differences of consecutive values in the path, plus the length of the path minus 1
        
        # So the problem is to find the minimum cost path from x to y, and the maximum length of such a path
        
        # This is a standard shortest path problem, where the cost of a path is the sum of the edge costs, and we need to find the shortest path and the longest path with that cost
        
        # But for large N and Q, this is not feasible with standard Dijkstra's algorithm
        
        # So we need to find an efficient way to compute this
        
        # Let's think about the cost function again
        
        # The cost of a path from x to y is the sum of |v_{i+1} - v_i| + 1 for each step in the path
        
        # Let's denote the sum of |v_{i+1} - v_i| as S, and the number of steps as k. Then the cost is S + (k-1)
        
        # So the cost is S + (k