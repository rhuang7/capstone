import sys
import heapq

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            Ai = int(data[idx])
            Bi = int(data[idx+1])
            Ci = int(data[idx+2])
            graph[Ai].append((Bi, Ci))
            graph[Bi].append((Ai, Ci))
            idx += 3
        # Dijkstra to find shortest distance from 1 to N
        dist = [float('inf')] * (N+1)
        dist[1] = 0
        heap = [(0, 1)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        # BFS to count number of shortest paths
        from collections import deque
        count = [0] * (N+1)
        count[1] = 1
        queue = deque([1])
        while queue:
            u = queue.popleft()
            for v, w in graph[u]:
                if dist[v] == dist[u] + w:
                    count[v] += count[u]
                    queue.append(v)
        print(count[N])

if __name__ == '__main__':
    solve()