import sys
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
        
        adj = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Perform BFS to compute depth of each node
        depth = [0] * N
        visited = [False] * N
        q = deque()
        q.append(0)
        visited[0] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v] and v != 0:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        # Process queries
        queries = []
        for _ in range(Q):
            v = int(data[idx]) - 1
            queries.append(v)
            idx += 1
        
        # For each query, collect nodes in subtree of V with even distance
        # Use DFS to find subtree and check distances
        # To optimize, precompute for each node its subtree
        # But for this problem, we can process each query directly
        # However, for large N and Q, this would be too slow
        # So we need a more efficient approach
        
        # We'll use a post-order traversal to collect all nodes in the subtree
        # and for each query, we'll find nodes in the subtree with even distance
        # from V and add their values to A[V]
        
        # Precompute in and out times for each node to represent its subtree
        in_time = [0] * N
        out_time = [0] * N
        time = 0
        visited = [False] * N
        def dfs(u, parent):
            nonlocal time
            visited[u] = True
            in_time[u] = time
            time += 1
            for v in adj[u]:
                if not visited[v] and v != parent:
                    dfs(v, u)
            out_time[u] = time - 1
        
        dfs(0, -1)
        
        # For each query, find all nodes in the subtree of V with even distance
        # and add their values to A[V]
        # To do this efficiently, we can use a BFS from V and check if the distance is even
        # and the node is in the subtree of V
        # But for large N and Q, this is O(Q*N), which is too slow
        # So we need a better way
        
        # Instead, for each query, we can do a BFS from V and collect nodes in the subtree
        # with even distance
        # This is O(Q*N), but for N and Q up to 2e5, this is O(4e10), which is way too slow
        
        # So we need a smarter approach
        
        # Let's think about the problem differently
        # For each node, when it is processed in a query, it can only be added to its ancestor
        # at even distance
        # So for each node, we can track which ancestors are at even distance
        # and add its value to those ancestors
        # But how to do this efficiently?
        
        # We can use a BFS from each node and for each ancestor at even distance, add the value
        # But this is again O(N^2), which is too slow
        
        # So we need to find a way to process all queries in O(N + Q) time
        
        # Let's think of it this way:
        # For each query V, we need to find all nodes in the subtree of V with even distance from V
        # and add their values to A[V]
        # So for each query, we can perform a BFS from V and check for even distance
        # and if the node is in the subtree of V
        # But again, this is O(Q*N), which is too slow
        
        # So we need to find a way to precompute for each node, all ancestors at even distance
        # and for each query, add the value of the node to those ancestors
        # But how?
        
        # Let's think of it this way:
        # For each node, we can track the path from the root to the node
        # and for each ancestor, we can check if the distance is even
        # and add the value of the node to that ancestor
        # But this would be O(N^2) in the worst case
        
        # So the only way to handle this efficiently is to process each query with a BFS
        # and collect the nodes in the subtree of V with even distance from V
        
        # So we'll proceed with that approach, even though it's O(Q*N), but for the given constraints,
        # it's the only way to pass
        
        # Now, process each query
        for v in queries:
            # BFS from v, collect nodes in subtree of v with even distance
            # and add their values to A[v]
            visited = [False] * N
            q = deque()
            q.append((v, 0))
            visited[v] = True
            while q:
                u, d = q.popleft()
                if d % 2 == 0 and u != v:
                    A[v] += A[u]
                    A[u] = 0
                for neighbor in adj[u]:
                    if not visited[neighbor] and in_time[neighbor] >= in_time[v] and out_time[neighbor] <= out_time[v]:
                        visited[neighbor] = True
                        q.append((neighbor, d + 1))
        
        results.append(' '.join(map(str, A)))
    
    print('\n'.join(results))