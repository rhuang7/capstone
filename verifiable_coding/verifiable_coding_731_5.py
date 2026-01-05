import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    C = int(data[idx])
    idx += 1
    F = int(data[idx])
    idx += 1
    
    graph = [[] for _ in range(C + 1)]
    
    for _ in range(F):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        p = int(data[idx])
        idx += 1
        graph[x].append((y, p))
        graph[y].append((x, p))
    
    max_cost = 0
    
    for start in range(1, C + 1):
        dist = [float('inf')] * (C + 1)
        dist[start] = 0
        heap = [(0, start)]
        
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue
            for neighbor, price in graph[node]:
                if dist[neighbor] > dist[node] + price:
                    dist[neighbor] = dist[node] + price
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        
        max_cost = max(max_cost, dist[start])
    
    print(max_cost)

if __name__ == '__main__':
    solve()