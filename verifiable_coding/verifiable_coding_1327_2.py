import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        v = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Preprocess for each node, the adjacent nodes in order
        # We'll use a list of lists for adjacency
        adj = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    cost = abs(v[j] - v[i]) + (j - i)
                    adj[i].append((j, cost))
        
        # For each query, we need to find:
        # 1. Minimum cost from x to y
        # 2. Maximum length of a path with that cost
        
        # Dijkstra's algorithm for minimum cost
        # We'll use a priority queue (heapq)
        # We'll also track the maximum length for each node
        # Since the graph is dense, we'll use a modified Dijkstra for each query
        
        for _ in range(Q):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            
            if x == y:
                results.append("-1 2")
                continue
            
            # Dijkstra for minimum cost
            dist = [float('inf')] * N
            dist[x] = 0
            prev = [-1] * N
            length = [0] * N
            heap = [(0, x)]
            
            while heap:
                cost, u = heapq.heappop(heap)
                if u == y:
                    break
                if cost > dist[u]:
                    continue
                for v, w in adj[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        prev[v] = u
                        length[v] = length[u] + 1
                        heapq.heappush(heap, (dist[v], v))
                    elif dist[v] == dist[u] + w:
                        if length[v] < length[u] + 1:
                            length[v] = length[u] + 1
            
            min_cost = dist[y]
            max_len = length[y]
            results.append(f"{min_cost} {max_len}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()