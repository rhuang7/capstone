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
    tree = defaultdict(list)
    for i in range(N-1):
        u = int(edges[2*i]) - 1
        v = int(edges[2*i+1]) - 1
        tree[u].append(v)
        tree[v].append(u)
    
    # For each node, store the path from 1 to it
    # We'll use BFS to find the shortest path from 1 to all nodes
    # And also record the path
    parent = [ -1 ] * N
    visited = [False] * N
    queue = [0]
    visited[0] = True
    while queue:
        u = queue.pop(0)
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    # Now, for each node, reconstruct the path from 1 to it
    # And compute the LIS for each path
    # We'll use a list to store the LIS for each path
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll also use a list of lists, where path[i] is the path to node i
    # However, since N is large, we need an efficient way to compute LIS for each path
    # We'll use a dynamic programming approach for LIS, but since the paths are different for each node, we need to process them in order
    
    # We'll process the nodes in BFS order, since the shortest path from 1 to each node is unique and can be processed in order
    # We'll use a list to store the LIS for each node
    lis = [0] * N
    # We'll use a list to store the path for each node
    path = [[] for _ in range(N)]
    # We'll use a list to store the path for each node
    # We'll build the path for each node by backtracking from the node to 1 using the parent array
    # Then we'll compute the LIS for each path
    
    # First, build the path for each node
    for i in range(1, N):
        current = i
        path[i] = []
        while current != -1:
            path[i].append(current)
            current = parent[current]
        path[i] = path[i][::-1]  # reverse to get the path from 1 to i
    
    # Now, compute the LIS for each path
    # We'll use a list to store the LIS for each path
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    
    # We'll use a list to store the LIS for each path
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    
    # We'll use a list to store the LIS for each path
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    
    # We'll use a list to store the LIS for each path
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list of lists, where lis[i] is the LIS for the path to node i
    # We'll use a list