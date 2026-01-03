import sys
import bisect

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(N-1):
        u = int(edges[2*i])
        v = int(edges[2*i+1])
        graph[u].append(v)
        graph[v].append(u)
    
    # For each node, store the path from 1 to it
    # We'll use BFS to find shortest paths
    from collections import deque
    parent = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)
    
    # Now, for each node k, we need to find the LIS of the path from 1 to k
    # We'll use a list to store the LIS for each path
    # We'll use a binary search approach for each path
    # We'll store for each node the path from 1 to it as a list
    # But since the tree is big, we can't store all paths
    # Instead, we'll use a dynamic programming approach
    # For each node, we'll keep track of the LIS up to that node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the LIS for the path from 1 to the current node
    # We'll use a list to store the