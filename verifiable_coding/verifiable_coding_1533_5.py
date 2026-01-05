import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    special = list(map(int, data[idx:idx+K]))
    idx += K
    
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        X = int(data[idx])
        idx += 1
        Y = int(data[idx])
        idx += 1
        Z = int(data[idx])
        idx += 1
        adj[X].append((Y, Z))
        adj[Y].append((X, Z))
    
    # Dijkstra's algorithm for all special nodes
    dist = [float('inf')] * (N + 1)
    dist_special = [float('inf')] * (N + 1)
    
    # Initialize distances for special nodes
    for node in special:
        dist_special[node] = 0
    
    # Priority queue: (distance, node)
    heap = []
    for node in special:
        heapq.heappush(heap, (0, node))
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist_special[u]:
            continue
        for v, w in adj[u]:
            if dist_special[v] > dist_special[u] + w:
                dist_special[v] = dist_special[u] + w
                heapq.heappush(heap, (dist_special[v], v))
    
    # Find the minimum distance between any two special nodes
    min_dist = float('inf')
    for i in range(len(special)):
        for j in range(i + 1, len(special)):
            u = special[i]
            v = special[j]
            if dist_special[v] < min_dist:
                min_dist = dist_special[v]
    
    print(min_dist)