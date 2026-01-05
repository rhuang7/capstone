import sys
import math

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
        # Initialize distance matrix
        dist = [[-1]*M for _ in range(N)]
        # BFS from all treasure cells
        from collections import deque
        q = deque()
        for x, y in treasure:
            dist[x][y] = 0
            q.append((x, y))
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if (nx, ny) not in blocked and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        # Print the result
        for i in range(N):
            row = []
            for j in range(M):
                if (i, j) in blocked:
                    row.append('X')
                else:
                    row.append(str(dist[i][j]))
            print(' '.join(row))
if __name__ == '__main__':
    solve()