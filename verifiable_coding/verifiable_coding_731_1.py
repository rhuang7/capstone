import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    C = int(data[0])
    F = int(data[1])
    
    graph = [[] for _ in range(C + 1)]
    index = 2
    for _ in range(F):
        x = int(data[index])
        y = int(data[index + 1])
        p = int(data[index + 2])
        graph[x].append((y, p))
        graph[y].append((x, p))
        index += 3
    
    # Floyd-Warshall algorithm to compute all pairs shortest paths
    dist = [[float('inf')] * (C + 1) for _ in range(C + 1)]
    for i in range(1, C + 1):
        dist[i][i] = 0
    
    for x in range(1, C + 1):
        for (y, p) in graph[x]:
            if dist[x][y] > p:
                dist[x][y] = p
    
    for k in range(1, C + 1):
        for i in range(1, C + 1):
            for j in range(1, C + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    max_cost = 0
    for i in range(1, C + 1):
        for j in range(i + 1, C + 1):
            if dist[i][j] > max_cost:
                max_cost = dist[i][j]
    
    print(max_cost)