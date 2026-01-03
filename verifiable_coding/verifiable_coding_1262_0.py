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
        X = int(data[idx])
        idx += 1
        treasure = set()
        for _ in range(X):
            x = int(data[idx]) - 1
            y = int(data[idx+1]) - 1
            treasure.add((x, y))
            idx += 2
        Y = int(data[idx])
        idx += 1
        blocked = set()
        for _ in range(Y):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            blocked.add((u, v))
            idx += 2
        dist = [[-1]*M for _ in range(N)]
        q = []
        for x, y in treasure:
            dist[x][y] = 0
            heapq.heappush(q, (0, x, y))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            d, x, y = heapq.heappop(q)
            if (x, y) in blocked:
                continue
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if dist[nx][ny] == -1 and (nx, ny) not in blocked:
                        dist[nx][ny] = d + 1
                        heapq.heappush(q, (d + 1, nx, ny))
        for i in range(N):
            row = []
            for j in range(M):
                if (i, j) in blocked:
                    row.append('X')
                else:
                    row.append(str(dist[i][j]))
            print(' '.join(row))
        if _ < T - 1:
            print()