import sys
import math

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
        X = int(data[idx])
        idx += 1
        treasure = set()
        for _ in range(X):
            x = int(data[idx])
            y = int(data[idx+1])
            treasure.add((x-1, y-1))
            idx += 2
        Y = int(data[idx])
        idx += 1
        blocked = set()
        for _ in range(Y):
            u = int(data[idx])
            v = int(data[idx+1])
            blocked.add((u-1, v-1))
            idx += 2
        dist = [[-1]*M for _ in range(N)]
        q = []
        for i in range(N):
            for j in range(M):
                if (i, j) in treasure:
                    dist[i][j] = 0
                    q.append((i, j))
                elif (i, j) in blocked:
                    dist[i][j] = 'X'
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            x, y = q.pop(0)
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if dist[nx][ny] == -1 and (nx, ny) not in blocked:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        for row in dist:
            print(' '.join(str(x) if x != 'X' else 'X' for x in row))
        
if __name__ == '__main__':
    solve()