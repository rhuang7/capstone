import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for i in range(0, len(edges), 2):
        u = int(edges[i]) - 1
        v = int(edges[i+1]) - 1
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to find depth of each node from the capital (node 0)
    depth = [-1] * N
    q = deque()
    q.append(0)
    depth[0] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                q.append(v)
    
    # Calculate the Grundy numbers for each node
    grundy = [0] * N
    for i in range(N-1, -1, -1):
        if depth[i] == 0:
            continue
        # The node is at depth d, and its parent is at depth d-1
        d = depth[i]
        parent = -1
        for neighbor in graph[i]:
            if depth[neighbor] == d - 1:
                parent = neighbor
                break
        # The number of soldiers in this node is S[i]
        # The Grundy number for this node is the mex of the grundy numbers of its parent
        # But since we can move soldiers from this node to its parent, the game is equivalent to a Nim heap of size S[i]
        # The Grundy number for this node is S[i] % (d + 1)
        grundy[i] = S[i] % (d + 1)
    
    # The total XOR of all grundy numbers is the overall Grundy number of the game
    total_xor = 0
    for i in range(N):
        total_xor ^= grundy[i]
    
    if total_xor != 0:
        print("First")
    else:
        print("Second")