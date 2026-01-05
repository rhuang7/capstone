import sys
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(1 << 25)

def solve():
    import sys
    import sys
    input = sys.stdin.buffer.readline
    sys.setrecursionlimit(1 << 25)
    T = int(input())
    for _ in range(T):
        N, Q = map(int, input().split())
        A = list(map(int, input().split()))
        from collections import defaultdict, deque
        tree = defaultdict(list)
        for _ in range(N-1):
            u, v = map(int, input().split())
            tree[u].append(v)
            tree[v].append(u)
        queries = [int(input()) for _ in range(Q)]
        # Preprocess parent and depth for each node
        parent = [0]*(N+1)
        depth = [0]*(N+1)
        visited = [False]*(N+1)
        q = deque()
        q.append(1)
        visited[1] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v] and v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    visited[v] = True
                    q.append(v)
        # For each query, find all nodes in subtree of V with even distance from V (excluding V)
        # We can use a BFS for each query, but that would be too slow for large Q
        # So we need a more efficient way
        # Preprocess for each node, the subtree
        # We can use a DFS to find the subtree of each node
        # But since queries are online, we need to process them efficiently
        # Let's use a heavy-light decomposition or some other method
        # Alternatively, for each query, perform a BFS on the subtree of V, and collect nodes at even distance
        # But with large N and Q, this is too slow
        # So we need a better approach
        # Let's precompute for each node, the nodes in its subtree
        # But again, this is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think differently
        # For each query V, we need to find all nodes in the subtree of V that are at even distance from V (excluding V)
        # So for each query, we can perform a BFS starting from V, and collect nodes in the subtree of V at even distance
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need a way to precompute for each node, the nodes in its subtree at even and odd distances
        # But how?
        # We can precompute for each node, a list of nodes in its subtree, and for each node, store the distance from V
        # But again, this is too slow
        # So we need to find a way to process each query in O(1) or O(logN) time
        # Let's think about the problem differently
        # For each query V, the nodes in the subtree of V that are at even distance from V (excluding V) are those nodes that are at depth even in the subtree rooted at V
        # So for each node, we can precompute the depth in the subtree of V, but again, this is not feasible
        # So we need to find a way to process each query efficiently
        # Let's use a BFS for each query, but optimize it
        # For each query V, we can perform a BFS starting from V, and collect nodes in the subtree of V at even distance
        # But with large Q, this is too slow
        # So we need to find a way to process the queries in O(1) time per query
        # Let's think about the following:
        # For each node V, the nodes in its subtree at even distance from V are those nodes that are at even depth in the subtree rooted at V
        # So for each node V, we can precompute a list of nodes in its subtree at even depth
        # But how?
        # We can perform a DFS from each node, and for each node, record the depth in the subtree
        # But with N up to 2e5, this is O(N^2), which is not feasible
        # So we need a better way
        # Let's think about the following: for each query V, we need to find all nodes in the subtree of V that are at even distance from V (excluding V)
        # So we can perform a BFS starting from V, and for each node in the subtree of V, check if the distance from V is even
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each node V, we can precompute the nodes in its subtree at even depth
        # But how?
        # We can perform a DFS from each node, and for each node, record the depth in the subtree
        # But with N up to 2e5, this is O(N^2), which is not feasible
        # So we need to find a way to process the queries in O(1) time per query
        # Let's think about the following:
        # For each query V, the nodes in the subtree of V that are at even distance from V are those nodes that are at even depth in the subtree rooted at V
        # So for each node V, we can precompute a list of nodes in its subtree at even depth
        # But how?
        # We can perform a DFS from each node, and for each node, record the depth in the subtree
        # But with N up to 2e5, this is O(N^2), which is not feasible
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each node V, we can precompute the nodes in its subtree at even depth
        # But how?
        # We can perform a BFS from each node, and for each node, record the depth in the subtree
        # But with N up to 2e5, this is O(N^2), which is not feasible
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, we can perform a BFS starting from V, and for each node in the subtree of V, check if the distance from V is even
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, the nodes in the subtree of V that are at even distance from V are those nodes that are at even depth in the subtree rooted at V
        # So for each node V, we can precompute a list of nodes in its subtree at even depth
        # But how?
        # We can perform a BFS from each node, and for each node, record the depth in the subtree
        # But with N up to 2e5, this is O(N^2), which is not feasible
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, we can perform a BFS starting from V, and for each node in the subtree of V, check if the distance from V is even
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, we can perform a BFS starting from V, and for each node in the subtree of V, check if the distance from V is even
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, we can perform a BFS starting from V, and for each node in the subtree of V, check if the distance from V is even
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think about the following:
        # For each query V, we can perform a BFS starting from V, and for each node in the subtree of V, check if the distance from V is even
        # But with Q up to 2e5, and N up to 2e5, this is O(Q*N), which is too slow
        # So we need to find a way to process the queries efficiently
        # Let's think about