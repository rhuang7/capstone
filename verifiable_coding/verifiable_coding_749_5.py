import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    costs = []
    index = 1
    for _ in range(N):
        row = list(map(int, data[index:index+N]))
        index += N
        costs.append(row)
    
    # Build a graph where each node is a city
    # We need to find a way to connect cities such that removing any one node leaves the rest connected
    # This is equivalent to finding a 2-edge-connected graph on N-1 nodes (since the capital is connected to all)
    # So we need to find a minimum spanning tree on the graph where the capital is connected to all others
    
    # We can model this as a minimum spanning tree problem on N-1 nodes (excluding the capital)
    # But since the capital is already connected to all, we can treat it as a single node and connect all other nodes to it
    
    # We can use Kruskal's algorithm to find the minimum cost to connect all nodes except the capital to the capital
    # But since the capital is already connected to all, we can ignore the capital in the MST
    # So we need to find the minimum spanning tree on the remaining N-1 nodes
    
    # Create a list of edges between all pairs of cities (excluding the capital)
    edges = []
    for i in range(1, N):
        for j in range(i+1, N):
            edges.append((costs[i-1][j-1], i, j))
    
    # Sort edges by cost
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(N))
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return False
        parent[root_v] = root_u
        return True
    
    total_cost = 0
    count = 0
    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            count += 1
            if count == N-1:
                break
    
    print(total_cost)

if __name__ == '__main__':
    solve()