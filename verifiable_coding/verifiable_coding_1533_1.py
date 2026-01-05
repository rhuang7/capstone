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
    
    dist = [float('inf')] * (N + 1)
    dist[special[0]] = 0
    heap = [(0, special[0])]
    visited = set()
    
    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    
    min_dist = float('inf')
    for i in range(1, K):
        min_dist = min(min_dist, dist[special[i]])
    
    print(min_dist)