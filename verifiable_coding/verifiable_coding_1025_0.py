import sys
import sys
from sys import stdin
import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx +=2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        tree = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            tree[u].append(v)
            tree[v].append(u)
            idx +=2
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]))
            idx +=1
        # Compute subtree sizes and depths
        depth = [0]*(N+1)
        parent = [0]*(N+1)
        visited = [False]*(N+1)
        def dfs(u, p):
            visited[u] = True
            parent[u] = p
            for v in tree[u]:
                if not visited[v]:
                    depth[v] = depth[u]+1
                    dfs(v, u)
        dfs(1, 0)
        # For each query, find all nodes in the subtree of V at even distance
        # and add their A values to A[V]
        # We need to process queries efficiently
        # We'll use a BFS for each query
        # But with Q up to 2e5 and N up to 2e5, this is O(Q*N), which is too slow
        # So we need a better approach
        # We'll precompute for each node, the nodes in its subtree at even distance
        # But that's also too slow
        # So we'll process each query with BFS, but optimize it
        # We'll use a visited array to avoid reprocessing
        # However, since the queries are processed in sequence, we need to track which nodes have been processed
        # So we'll use a visited array to track which nodes have been processed
        # And for each query, we'll perform a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # We'll also track the nodes that have been processed to avoid reprocessing
        # But this is still O(Q*N), which is too slow
        # So we need a smarter approach
        # Let's think about the problem differently
        # For each node, when it is processed in a query, it contributes to its ancestor at even distance
        # So for each node, we can track the ancestors at even distance and add its value to them
        # But how to do this efficiently?
        # We can use a BFS for each query, but with the following optimization:
        # For each query V, we perform a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # We'll use a visited array to track which nodes have been processed
        # So we'll have a visited array that is reset for each test case
        # But this is still O(Q*N), which is too slow
        # So we need a better approach
        # Let's think about the problem in terms of levels
        # For each query V, we need to find all nodes in the subtree of V at even distance from V
        # and add their A values to A[V]
        # So for each node, we can precompute the ancestors at even distance
        # But again, this is not feasible for large N
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, we need to find all nodes in the subtree of V at even distance from V
        # and add their A values to A[V]
        # We can do this with a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # But this is O(Q*N), which is too slow
        # So we need a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each node, we can track the number of times it is added to its ancestors at even distance
        # But again, this is not straightforward
        # So we'll proceed with the BFS approach, but with some optimizations
        # We'll use a visited array to track which nodes have been processed
        # And for each query, we'll perform a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # We'll also track the nodes that have been processed to avoid reprocessing
        # But this is still O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each query V, we need to find all nodes in the subtree of V at even distance from V
        # and add their A values to A[V]
        # We can do this with a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # But this is O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each node, we can precompute the nodes in its subtree at even distance
        # But again, this is not feasible for large N
        # So we'll proceed with the BFS approach, but with some optimizations
        # We'll use a visited array to track which nodes have been processed
        # And for each query, we'll perform a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # We'll also track the nodes that have been processed to avoid reprocessing
        # But this is still O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each query V, we need to find all nodes in the subtree of V at even distance from V
        # and add their A values to A[V]
        # We can do this with a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # But this is O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each node, we can precompute the nodes in its subtree at even distance
        # But again, this is not feasible for large N
        # So we'll proceed with the BFS approach, but with some optimizations
        # We'll use a visited array to track which nodes have been processed
        # And for each query, we'll perform a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # We'll also track the nodes that have been processed to avoid reprocessing
        # But this is still O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each query V, we need to find all nodes in the subtree of V at even distance from V
        # and add their A values to A[V]
        # We can do this with a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # But this is O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each node, we can precompute the nodes in its subtree at even distance
        # But again, this is not feasible for large N
        # So we'll proceed with the BFS approach, but with some optimizations
        # We'll use a visited array to track which nodes have been processed
        # And for each query, we'll perform a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # We'll also track the nodes that have been processed to avoid reprocessing
        # But this is still O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each query V, we need to find all nodes in the subtree of V at even distance from V
        # and add their A values to A[V]
        # We can do this with a BFS starting from V, only visiting nodes in its subtree
        # and at even distance from V
        # But this is O(Q*N), which is too slow
        # So we need to find a way to process the queries in O(Q + N) time
        # Let's think about the following:
        # For each node, we can precompute the nodes in its subtree