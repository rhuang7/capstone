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
        for i, j in treasure:
            dist[i][j] = 0
            heapq.heappush(q, (0, i, j))
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            d, i, j = heapq.heappop(q)
            if (i, j) in blocked:
                continue
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    if dist[ni][nj] == -1 and (ni, nj) not in blocked:
                        dist[ni][nj] = d + 1
                        heapq.heappush(q, (d+1, ni, nj))
        
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