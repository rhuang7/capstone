import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx]); idx +=1
    M = int(data[idx]); idx +=1
    W = int(data[idx]); idx +=1
    K = int(data[idx]); idx +=1
    R = int(data[idx]); idx +=1

    grid = [[-1 for _ in range(M)] for _ in range(N)]
    for _ in range(W):
        x1 = int(data[idx])-1; idx +=1
        y1 = int(data[idx])-1; idx +=1
        x2 = int(data[idx])-1; idx +=1
        y2 = int(data[idx])-1; idx +=1
        if x1 == x2:
            if y1 < y2:
                grid[x1][y1] = -2
                grid[x1][y2] = -2
            else:
                grid[x1][y2] = -2
                grid[x1][y1] = -2
        else:
            if x1 < x2:
                grid[x1][y1] = -2
                grid[x2][y1] = -2
            else:
                grid[x2][y1] = -2
                grid[x1][y1] = -2

    room_id = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == -1 and not visited[i][j]:
                queue = collections.deque()
                queue.append((i, j))
                visited[i][j] = True
                grid[i][j] = room_id
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == -1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            grid[nx][ny] = room_id
                            queue.append((nx, ny))
                room_id +=1

    support = {}
    for _ in range(R):
        x = int(data[idx])-1; idx +=1
        y = int(data[idx])-1; idx +=1
        c1 = int(data[idx]); idx +=1
        c2 = int(data[idx]); idx +=1
        support[(x, y)] = (c1, c2)

    room_support = [0]*room_id
    for (x, y), (c1, c2) in support.items():
        room_support[grid[x][y]] = (c1, c2)

    cost = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] != -1:
                c1, c2 = room_support[grid[i][j]]
                cost += min(c1, c2)

    for i in range(N):
        for j in range(M):
            if grid[i][j] != -1:
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != -1 and grid[i][j] != grid[nx][ny]:
                        cost += K

    print(cost)

if __name__ == '__main__':
    solve()