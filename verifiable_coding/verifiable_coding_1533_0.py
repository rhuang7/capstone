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
    heap = []
    
    for node in special:
        dist[node] = 0
        heapq.heappush(heap, (0, node))
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    min_dist = float('inf')
    for i in range(len(special)):
        for j in range(i + 1, len(special)):
            u = special[i]
            v = special[j]
            if dist[u] + dist[v] < min_dist:
                min_dist = dist[u] + dist[v]
    
    print(min_dist)