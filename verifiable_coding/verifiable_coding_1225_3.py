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
            idx += 3
            graph[Ai].append((Bi, Ci))
            graph[Bi].append((Ai, Ci))
        dist = [float('inf')] * (N+1)
        dist[1] = 0
        count = [0] * (N+1)
        count[1] = 1
        heap = [(0, 1)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, c in graph[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    count[v] = count[u]
                    heapq.heappush(heap, (dist[v], v))
                elif dist[v] == dist[u] + c:
                    count[v] += count[u]
        print(count[N])

if __name__ == '__main__':
    solve()