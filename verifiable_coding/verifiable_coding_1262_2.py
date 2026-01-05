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
        grid = [[-1 for _ in range(M)] for _ in range(N)]
        q = []
        for x, y in treasure:
            grid[x][y] = 0
            heapq.heappush(q, (0, x, y))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            dist, x, y = heapq.heappop(q)
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if (nx, ny) not in blocked and grid[nx][ny] == -1:
                        grid[nx][ny] = dist + 1
                        heapq.heappush(q, (dist + 1, nx, ny))
        for row in grid:
            print(' '.join(str(x) if x != -1 else 'X' for x in row))
        
if __name__ == '__main__':
    solve()