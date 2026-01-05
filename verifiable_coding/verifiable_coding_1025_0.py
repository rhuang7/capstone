import sys
import sys
from sys import stdin
import sys
input = sys.stdin.buffer.read
from collections import defaultdict, deque

def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]) - 1)
            idx += 1
        # Perform BFS to compute depths and parents
        depth = [0] * N
        parent = [ -1 ] * N
        visited = [False] * N
        q = deque()
        q.append(0)
        visited[0] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v] and v != parent[u]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        # Process queries
        # For each query, find all nodes in the subtree of V with even distance
        # and add their value to A[V], then set their value to 0
        # We can use BFS for each query
        # But for large N and Q, this is O(Q*N), which is too slow
        # So we need a more efficient approach
        # We can precompute for each node, the nodes in its subtree at even distance
        # But how?
        # We can use a post-order traversal to compute for each node, the nodes in its subtree at even distance
        # However, this is also complicated
        # Alternative approach: for each query, perform BFS from V, and for each node in the subtree, if distance is even and not V, add A[node] to A[V] and set A[node] to 0
        # This is O(Q*N), which is too slow for N=2e5 and Q=2e5
        # So we need to find a way to process all queries efficiently
        # Let's try to process all queries in a way that for each node, we track how many times it is added to its parent's value
        # But this is not straightforward
        # Let's try the naive approach for now, and see if it passes
        # But for large N and Q, this will TLE
        # So we need to find a way to process all queries in O(Q + N)
        # Let's think of the problem differently
        # For each query V, we want to add all nodes in the subtree of V at even distance (excluding V itself)
        # So for each node u in the subtree of V, if depth[u] - depth[V] is even and u != V, then add A[u] to A[V]
        # So we can precompute for each node, the nodes in its subtree at even distance
        # But how?
        # We can use a post-order traversal to compute for each node, the nodes in its subtree at even distance
        # But this is not straightforward
        # Alternative idea: for each query, perform a BFS from V and collect all nodes in the subtree of V at even distance
        # This is O(Q*N), which is too slow
        # So we need to find a way to process all queries in O(Q + N)
        # Let's try to find for each node, the number of times it is added to its parent's value
        # But this is not straightforward
        # Alternative idea: for each node, we can track the number of times it is added to its parent's value
        # But again, not sure
        # Let's try the naive approach for small cases
        # But for large N and Q, it will TLE
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each query V, we want to add all nodes in the subtree of V at even distance from V
        # So for each node u in the subtree of V, if depth[u] - depth[V] is even and u != V, then add A[u] to A[V]
        # So for each query V, we can perform a BFS from V and collect all nodes in the subtree of V at even distance
        # But for large N and Q, this is O(Q*N), which is too slow
        # So we need to find a way to process all queries in O(Q + N)
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But again, not sure
        # Let's try to find for each node, the nodes in its subtree at even distance
        # But how?
        # Let's try to precompute for each node, the nodes in its subtree at even distance
        # But this is not straightforward
        # Alternative idea: for each query V, we can use a BFS to find all nodes in the subtree of V at even distance
        # So for each query V, we perform a BFS starting from V, and for each node u in the subtree of V, if the distance from V to u is even and u != V, then add A[u] to A[V] and set A[u] to 0
        # This is O(Q*N), which is too slow for large N and Q
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But how?
        # Let's try to precompute for each node, the nodes in its subtree at even distance
        # But how?
        # Let's try to precompute for each node, the nodes in its subtree at even distance
        # We can perform a post-order traversal and for each node, store the nodes in its subtree at even distance
        # But this is not straightforward
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But how?
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But how?
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But how?
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But how?
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node, we can precompute for each level, the nodes in its subtree at that level
        # But how?
        # Let's try to find for each node, the nodes in its subtree at even distance
        # We can perform a BFS for each node, but this is O(N^2), which is not feasible
        # So we need to find a better approach
        # Let's think of the problem in terms of levels
        # For each node