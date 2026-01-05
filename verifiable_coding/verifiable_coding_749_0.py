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
    
    # Build a graph
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                graph[i].append((j, costs[i][j]))
    
    # Prim's algorithm to find minimum spanning tree (MST)
    # We need to ensure that removing any one city still leaves the rest connected
    # This is equivalent to finding a MST that is 2-edge-connected
    # So we need to find a MST that is 2-edge-connected, which can be done by finding a MST and then adding edges to make it 2-edge-connected
    
    # First, find MST of the graph
    mst = set()
    visited = [False] * N
    visited[0] = True
    min_heap = [(0, 0)]  # (cost, node)
    
    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst.add((u, v))
                mst.add((v, u))
    
    # Now, find the minimum number of edges to add to make the MST 2-edge-connected
    # This is equivalent to finding a minimum spanning tree of the graph with the edges not in the MST
    # We can use Krusky's algorithm for this
    
    # Create a list of edges not in the MST
    edges = []
    for i in range(N):
        for j in range(N):
            if i != j and (i, j) not in mst and (j, i) not in mst:
                edges.append((costs[i][j], i, j))
    
    # Sort the edges by cost
    edges.sort()
    
    # Use Union-Find to find the minimum number of edges to add
    parent = list(range(N))
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        pu = find(u)
        pv = find(v)
        if pu == pv:
            return False
        parent[pu] = pv
        return True
    
    result = 0
    for cost, u, v in edges:
        if union(u, v):
            result += cost
    
    print(result)

if __name__ == '__main__':
    solve()