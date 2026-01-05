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
        
        # Precompute for each node, the best path to all other nodes
        # We'll use Dijkstra's algorithm for each node
        # But since N is large, we need an efficient way
        # However, given the constraints, we can't do O(N^2) for each query
        
        # Instead, we'll use a modified Dijkstra for each query
        # But since Q is large, we need a better approach
        
        # We'll precompute for each node, the best path to all other nodes
        # But given the constraints, we can't do that for all nodes
        
        # So, we'll use a modified Dijkstra for each query
        # But since Q is large, we need to optimize
        
        # Let's use a priority queue for each query
        # We'll store the minimum cost and maximum length for each node
        
        for _ in range(Q):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            idx += 2
            
            # Dijkstra's algorithm for the minimum cost path
            # We'll track the minimum cost and the maximum length for each node
            dist = [float('inf')] * N
            length = [0] * N
            dist[x] = 0
            visited = [False] * N
            pq = [(0, x, 0)]  # (cost, node, length)
            
            while pq:
                cost, u, l = heapq.heappop(pq)
                if visited[u]:
                    continue
                visited[u] = True
                if u == y:
                    break
                for v in range(N):
                    if u == v:
                        continue
                    new_cost = cost + abs(v[i] - v[u]) + (v - u)
                    new_len = l + 1
                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        length[v] = new_len
                        heapq.heappush(pq, (new_cost, v, new_len))
            
            # Now find the maximum length for the minimum cost
            min_cost = dist[y]
            max_len = 0
            for i in range(N):
                if dist[i] == min_cost:
                    max_len = max(max_len, length[i])
            
            results.append(f"{min_cost} {max_len}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()