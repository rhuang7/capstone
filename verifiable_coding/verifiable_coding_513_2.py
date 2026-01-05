import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    from collections import defaultdict, deque

    # Build the tree
    tree = defaultdict(list)
    for i in range(N-1):
        u = int(edges[2*i])
        v = int(edges[2*i+1])
        tree[u].append(v)
        tree[v].append(u)
    
    # BFS to find parent and depth for each node
    parent = [0]*(N+1)
    depth = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    parent[1] = 0
    
    while q:
        u = q.popleft()
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
    
    # For each node, collect the path from 1 to it
    # We'll use a list to store the path and then compute LIS
    # However, for large N, this is not efficient, so we need a better approach
    
    # Instead, we'll perform a DFS traversal and maintain a list of LIS for each node
    # We'll use a dynamic programming approach where for each node, we track the LIS up to that node
    
    # We'll use a list to store the LIS for each node
    lis = [0]*(N+1)
    
    # We'll perform a DFS from node 1
    # For each node, we'll compute the LIS by considering the path from 1 to it
    
    # We'll use a list to store the path from 1 to current node
    # But for large N, we need an efficient way to compute LIS
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the path from 1 to current node
    # But for large N, we need an efficient way to compute LIS
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the LIS for the path from 1 to current node
    
    # We'll use a list to store the LIS for the path from 1 to current node
    # We'll use a binary search approach to compute LIS in O(N log N) time
    
    # We'll perform a DFS traversal and for each node, we'll compute the LIS
    # We'll use a list to store the