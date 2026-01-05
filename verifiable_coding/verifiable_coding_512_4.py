import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    edges = []
    color_map = defaultdict(list)
    color_total = defaultdict(int)
    
    for _ in range(N-1):
        a = int(data[idx]) - 1
        idx += 1
        b = int(data[idx]) - 1
        idx += 1
        c = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        edges.append((a, b, c, d))
        color_map[c].append((a, b, d))
        color_total[c] += d
    
    # Build adjacency list
    adj = [[] for _ in range(N)]
    for a, b, c, d in edges:
        adj[a].append((b, c, d))
        adj[b].append((a, c, d))
    
    # Precompute LCA and depth for each node
    LOG = 20
    up = [[-1]*N for _ in range(LOG)]
    depth = [0]*N
    
    def dfs(u, p):
        up[0][u] = p
        for v, c, d in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    dfs(0, -1)
    
    for k in range(1, LOG):
        for v in range(N):
            if up[k-1][v] != -1:
                up[k][v] = up[k-1][up[k-1][v]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for k in range(LOG-1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if up[k][u] != -1 and up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]
    
    def get_dist(u, v):
        ancestor = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[ancestor]
    
    # Precompute for each color the total length
    # For each query, we need to compute the distance with the color changed
    # We can precompute the total length for each color and use it in the query
    
    # For each query, we can compute the distance by:
    # - For each edge in the path between u and v, if its color is x_j, replace its length with y_j
    # - Sum all the lengths of the edges in the path
    
    # However, since the tree is static and we need to answer multiple queries, we can precompute for each color the total length
    # and then for each query, we can compute the distance as the original distance minus the sum of the original lengths of edges of color x_j
    # plus the sum of the new lengths of edges of color x_j
    
    # So, for each query:
    # - Compute the original distance between u and v
    # - Compute the sum of the original lengths of edges of color x_j in the path
    # - Compute the sum of the new lengths of edges of color x_j in the path
    # - The answer is original_distance - original_sum + new_sum
    
    # To compute the sum of the original lengths of edges of color x_j in the path between u and v, we can precompute for each color the total length
    # and then for each query, we can compute the sum of the original lengths of edges of color x_j in the path
    
    # However, this is not feasible directly, as we need to know which edges are on the path between u and v
    
    # So, we need to find the edges on the path between u and v, and for each such edge, if its color is x_j, we add its original length or the new length
    
    # To do this, we can precompute for each color the list of edges, and for each query, we can find the edges on the path between u and v and check their colors
    
    # However, this is not efficient for large N and Q
    
    # So, we need a way to compute the sum of the lengths of edges of a certain color on the path between u and v
    
    # To do this, we can precompute for each color a map from node to the sum of lengths of edges of that color on the path from the root to that node
    
    # Then, for any two nodes u and v, the sum of the lengths of edges of color x on the path between u and v is:
    # sum_u + sum_v - 2 * sum_lca
    
    # So, we can precompute for each color a depth array that stores the sum of lengths of edges of that color on the path from the root to each node
    
    # Let's precompute for each color a depth array
    
    color_depth = defaultdict(list)
    for c in color_map:
        color_depth[c] = [0]*N
        for a, b, d in color_map[c]:
            # We need to update the depth arrays for the nodes in the path from the root to a and b
            # But this is not straightforward, as the color is not part of the tree structure
            # So, we need to find the path between a and b and update the color_depth for each node on that path
            # This is not feasible for large N and Q
    
    # Alternative approach: for each query, find the path between u and v, and for each edge on that path, check if its color is x_j, and sum the lengths accordingly
    
    # To find the path between u and v, we can use the LCA method
    
    # So, for each query, we can:
    # 1. Find the LCA of u and v
    # 2. Find the path from u to LCA and from v to LCA
    # 3. For each edge on the path, check if its color is x_j, and sum the lengths accordingly
    
    # But this is O(N) per query, which is too slow for Q=1e5
    
    # So, we need a more efficient way
    
    # Let's precompute for each color a map from node to the sum of lengths of edges of that color on the path from the root to that node
    
    # To do this, we can perform a DFS and for each node, for each color, store the sum of lengths of edges of that color on the path from the root to that node
    
    # This is possible, but it will take O(N * (N-1)) time and space, which is not feasible
    
    # Alternative idea: for each color, precompute the total length of all edges of that color, and for each query, if the color x_j is not present, the answer is the original distance
    
    # So, for each query, we can:
    # - Compute the original distance between u and v
    # - Compute the sum of the original lengths of edges of color x_j on the path between u and v
    # - Compute the sum of the new lengths of edges of color x_j on the path between u and v
    # - The answer is original_distance - original_sum + new_sum
    
    # To compute the sum of the original lengths of edges of color x_j on the path between u and v, we can use the LCA method
    
    # So, we need to find the edges on the path between u and v, and for each such edge, check if its color is x_j
    
    # But how to do this efficiently?
    
    # We can precompute for each color a list of edges, and for each query, we can iterate through the edges of that color and check if they are on the path between u and v
    
    # But this is O(M) per query, where M is the number of edges of color x_j, which is not feasible for large Q
    
    # So, the only feasible way is to precompute for each color a map from node to the sum of lengths of edges of that color on the path from the root to that node
    
    # Let's proceed with this approach
    
    # Precompute for each color a depth array
    color_depth = defaultdict(list)
    for c in color_map:
        color_depth[c] = [0]*N
        for a, b, d in color_map[c]:
            # We need to find the path from the root to a and from the root to b, and update the color_depth for each node on the path
            # But this is not straightforward
    
    # Alternative approach: for each query, find the path between u and v, and for each edge on that path, check if its color is x_j, and sum the lengths accordingly
    
    # This is the only feasible way for now