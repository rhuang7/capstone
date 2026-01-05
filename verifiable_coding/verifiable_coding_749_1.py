import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    cost = []
    index = 1
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(data[index]))
            index += 1
        cost.append(row)
    
    # Build a minimum spanning tree (MST) of the graph excluding the capital (node 1)
    # Since the capital is already connected to all other cities, we need to connect the remaining cities
    # such that removing any single node doesn't disconnect the graph. This is equivalent to finding
    # a MST of the graph with node 1 removed, and then adding the minimum cost edges to connect the remaining nodes.
    
    # Create a graph with nodes 2 to N
    # Use Prim's algorithm to find MST of this graph
    # We'll use a priority queue to select the next minimum edge
    
    # Initialize adjacency list
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and cost[i][j] > 0:
                adj[i].append((j, cost[i][j]))
    
    # Prim's algorithm
    visited = [False] * N
    min_cost = 0
    pq = []
    
    # Start from node 0 (capital)
    heapq.heappush(pq, (0, 0))
    visited[0] = True
    
    while pq:
        dist, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        min_cost += dist
        
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
    
    # The MST of the graph with node 0 (capital) removed is the answer
    print(min_cost)

if __name__ == '__main__':
    solve()