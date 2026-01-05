import sys
import heapq

def solve():
    import sys
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
        prev = [None] * (N+1)
        visited = [False] * (N+1)
        heap = [(0, 1)]
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    prev[v] = u
                    heapq.heappush(heap, (dist[v], v))
        # Count the number of shortest paths
        count = [0] * (N+1)
        count[1] = 1
        for i in range(2, N+1):
            if dist[i] == float('inf'):
                continue
            if prev[i] is None:
                continue
            if dist[prev[i]] + graph[prev[i]][i][1] == dist[i]:
                count[i] = count[prev[i]]
            else:
                count[i] = 0
        print(count[N])

if __name__ == '__main__':
    solve()