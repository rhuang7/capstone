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

    rooms = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == -1:
                queue = collections.deque()
                queue.append((i,j))
                grid[i][j] = len(rooms)
                rooms.append(set())
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == -1:
                            grid[nx][ny] = len(rooms)-1
                            rooms[-1].add((nx, ny))
                            queue.append((nx, ny))

    support = {}
    for _ in range(R):
        x = int(data[idx])-1; idx +=1
        y = int(data[idx])-1; idx +=1
        c1 = int(data[idx]); idx +=1
        c2 = int(data[idx]); idx +=1
        support[(x,y)] = (c1, c2)

    room_cost = [0]*len(rooms)
    for i in range(len(rooms)):
        for (x,y) in rooms[i]:
            c1, c2 = support[(x,y)]
            room_cost[i] += min(c1, c2)

    from collections import defaultdict
    adj = defaultdict(list)
    for i in range(N):
        for j in range(M):
            if grid[i][j] != -1:
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != -1:
                        if grid[i][j] != grid[nx][ny]:
                            adj[grid[i][j]].append(grid[nx][j])
                            adj[grid[nx][j]].append(grid[i][j])

    from collections import deque
    dp = [0]*len(rooms)
    for i in range(len(rooms)):
        dp[i] = room_cost[i]

    for i in range(len(rooms)):
        for j in adj[i]:
            if j > i:
                dp[j] = min(dp[j], dp[i] + room_cost[j] - room_cost[i])

    total = sum(dp)
    print(total + K * sum(len(adj[i]) for i in range(len(rooms))) // 2)

if __name__ == '__main__':
    solve()