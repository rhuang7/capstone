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
        
        # Precompute for each node, the best paths to and from other nodes
        # We'll use BFS for shortest path and DFS for longest path
        # But given the constraints, we need a more efficient approach
        
        # For each query, we need to find:
        # 1. Minimum cost from x to y
        # 2. Maximum length of such path
        
        # We'll use Dijkstra's algorithm for minimum cost (since the cost can be negative)
        # But since the graph is complete, we can optimize
        
        # For each query, we'll run Dijkstra's algorithm from x to y
        # However, with Q up to 2e5 and N up to 2e5, this would be too slow
        
        # So we need a better approach
        
        # Let's think about the cost function:
        # f(x, y) = |v_y - v_x| + y - x
        # This can be rewritten as:
        # f(x, y) = (y - x) + |v_y - v_x|
        
        # So the cost from x to y directly is (y - x) + |v_y - v_x|
        
        # Now, for a path from x to y, the total cost is the sum of these values along the path
        
        # Let's think about the minimum cost path:
        # Since the cost is additive, and the graph is complete, the minimum cost path is likely to be the direct path
        # Because any detour would add more cost (since the cost is always non-negative)
        
        # Wait, no! The cost can be negative. For example, if v_y is very small and y is very small, then the cost could be negative.
        
        # So we need to find the minimum cost path from x to y, which could involve going through other nodes.
        
        # However, with N up to 2e5 and Q up to 2e5, we can't run Dijkstra's for each query.
        
        # So we need to find a way to compute the minimum cost and maximum length for each query efficiently.
        
        # Let's think about the minimum cost:
        # The cost of a path from x to y is the sum of f(a_i, a_{i+1}) for each step.
        # Which is sum(|v_{a_{i+1}} - v_{a_i}| + (a_{i+1} - a_i))
        # = sum(|v_{a_{i+1}} - v_{a_i}|) + sum(a_{i+1} - a_i)
        # = sum(|v_{a_{i+1}} - v_{a_i}|) + (a_k - a_1)
        
        # So the total cost is (a_k - a_1) + sum(|v_{a_{i+1}} - v_{a_i}|)
        
        # Since a_k is y and a_1 is x, the first term is (y - x)
        # So the total cost is (y - x) + sum(|v_{a_{i+1}} - v_{a_i}|)
        
        # Therefore, the minimum cost path from x to y is the path that minimizes the sum of absolute differences between consecutive nodes.
        
        # This is the same as finding the path from x to y that minimizes the sum of absolute differences between consecutive nodes.
        
        # This is equivalent to finding the shortest path in a graph where the edge weight is |v_y - v_x|, and the path is from x to y.
        
        # So we can model this as a graph where the edge weight between x and y is |v_y - v_x|, and we need to find the shortest path from x to y.
        
        # However, with N up to 2e5, we can't run Dijkstra's for each query.
        
        # So we need to find a way to precompute for all pairs (x, y) the minimum cost and maximum length.
        
        # But with N up to 2e5, this is impossible.
        
        # So we need to find an efficient way to answer each query.
        
        # Let's think about the minimum cost:
        # The minimum cost is (y - x) + the minimum sum of absolute differences between consecutive nodes in a path from x to y.
        
        # The minimum sum of absolute differences is achieved by going from x to y directly, since any detour would add more absolute differences.
        
        # Therefore, the minimum cost is (y - x) + |v_y - v_x|
        
        # Wait, but what if there is a path that goes through other nodes and has a lower sum of absolute differences?
        
        # For example, if v_x = 10, v_y = 20, and there is a node v_z = 15. Then the direct path is 10 to 20: sum is 10.
        # The path x -> z -> y is 5 + 5 = 10. Same cost.
        # But if there is a node with v = 5, then x -> z -> y would be 5 + 15 = 20, which is worse.
        
        # So the minimum sum of absolute differences is achieved by going directly from x to y.
        
        # Therefore, the minimum cost is (y - x) + |v_y - v_x|
        
        # So for each query, the minimum cost is (y - x) + |v[y-1] - v[x-1]|
        
        # Now for the maximum length of such path:
        # The maximum length is the length of the path that achieves this minimum cost.
        
        # The direct path has length 2.
        # But there may be other paths with the same cost but longer length.
        
        # For example, in the sample input, the direct path from 2 to 3 has cost 4, but there is a longer path (length 3) with the same cost.
        
        # So we need to find the longest path that has the same minimum cost.
        
        # How can we do this efficiently?
        
        # Let's think about the cost function again.
        # The cost of a path is (y - x) + sum of absolute differences between consecutive nodes.
        # So the minimum cost is (y - x) + minimum sum of absolute differences.
        
        # The minimum sum of absolute differences is achieved by the direct path.
        
        # So the minimum cost is (y - x) + |v[y-1] - v[x-1]|
        
        # Now, for the maximum length of such path:
        # The maximum length is the length of the longest path that has this minimum cost.
        
        # How can we find this?
        
        # We need to find the longest path from x to y that has the same minimum cost.
        
        # But how can we do this efficiently?
        
        # Let's think about the cost function again.
        # The cost of a path is (y - x) + sum of absolute differences between consecutive nodes.
        # So for a path to have the same minimum cost, the sum of absolute differences must be the same as the direct path.
        
        # So the sum of absolute differences must be equal to |v[y-1] - v[x-1]|.
        
        # So the path must have the same sum of absolute differences as the direct path.
        
        # How can we find the longest path that has this property?
        
        # This is a problem of finding the longest path in a graph where the edge weights are |v_y - v_x|, and the sum of the edge weights must be equal to |v[y-1] - v[x-1]|.
        
        # But with N up to 2e5 and Q up to 2e5, this is not feasible with standard methods.
        
        # So we need to find a way to find the maximum length of such a path.
        
        # Let's think about the problem again.
        # The cost of a path is (y - x) + sum of absolute differences between consecutive nodes.
        # The minimum cost is (y - x) + |v[y-1] - v[x-1]|.
        
        # So the sum of absolute differences must be equal to |v[y-1] - v[x-1]|.
        
        # How can we find the longest path with this property?
        
        # The maximum length is the number of nodes in the path.
        
        # So we need to find the longest path from x to y where the sum of absolute differences between consecutive nodes is equal to |v[y-1] - v[x-1]|.
        
        # This seems like a problem that can be solved with BFS or DFS, but with large N and Q, this is not feasible.
        
        # So we need to find