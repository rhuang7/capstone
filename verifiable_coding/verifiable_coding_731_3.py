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
    
    # Dijkstra's algorithm for all pairs
    max_cost = 0
    for start in range(1, C + 1):
        dist = [float('inf')] * (C + 1)
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > dist[u]:
                continue
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap, (dist[v], v))
        max_cost = max(max_cost, dist[start])
    
    print(max_cost)

if __name__ == '__main__':
    solve()