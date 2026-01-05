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
    
    # Build the tree
    tree = defaultdict(list)
    for i in range(0, len(edges), 2):
        u = int(edges[i]) - 1
        v = int(edges[i+1]) - 1
        tree[u].append(v)
        tree[v].append(u)
    
    # Compute the depth of each node and the distance from the root (capital)
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
                parent[v] = u
                depth[v] = depth[u] + 1
                visited[v] = True
                q.append(v)
    
    # Compute the number of moves each node can contribute
    # Each node at depth d can contribute d moves (each move reduces the depth by 1)
    # We use a priority queue to simulate the game
    # The game is a variant of the Nim game where each pile has a size equal to the depth of the node
    # The player who takes the last move wins
    
    # Create a priority queue (max heap) of the depths
    # We use negative values to simulate a max heap with heapq
    heap = []
    for i in range(N):
        if i != 0:
            heapq.heappush(heap, -depth[i])
    
    # Game is a variant of Nim where the player can take from any pile
    # The Grundy number for each pile is its size
    # The XOR of all pile sizes determines the winner
    xor_sum = 0
    while heap:
        xor_sum ^= -heapq.heappop(heap)
    
    if xor_sum != 0:
        print("First")
    else:
        print("Second")