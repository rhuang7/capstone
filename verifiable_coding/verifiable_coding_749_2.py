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
    
    # The initial graph is a star with the capital (node 1) connected to all other nodes
    # We need to make it 2-connected: removing any single node should not disconnect the graph
    # This is equivalent to finding a minimum spanning tree of the graph with the capital as a node
    # But since the capital is already connected to all other nodes, we need to add edges to make the graph 2-connected
    # This is equivalent to finding a minimum spanning tree of the graph with the capital as a node, but with the capital connected to all other nodes
    # So we can treat the capital as a node and connect it to all other nodes, then find a minimum spanning tree of the graph
    
    # Create a new graph where the capital is node 0, and other nodes are 1 to N-1
    # The cost between node 0 and node i is cost[i][0]
    # The cost between node i and node j is cost[i][j]
    
    # Build the graph
    graph = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == 0:
                row.append(cost[j][0])
            else:
                row.append(cost[i][j])
        graph.append(row)
    
    # Kruskal's algorithm
    # Create a list of edges
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            edges.append((graph[i][j], i, j))
    
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
    
    # Kruskal's algorithm
    total_cost = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += cost
    
    print(total_cost)

if __name__ == '__main__':
    solve()