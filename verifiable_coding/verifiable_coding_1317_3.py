import sys
import collections

def main():
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
                queue.append((i, j))
                grid[i][j] = len(rooms)
                rooms.append(set())
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
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
        support[(x, y)] = (c1, c2)

    room_to_cells = [set() for _ in range(len(rooms))]
    for i in range(N):
        for j in range(M):
            room_to_cells[grid[i][j]].add((i, j))

    cost = [0]*len(rooms)
    for i in range(len(rooms)):
        for (x, y) in room_to_cells[i]:
            c1, c2 = support[(x, y)]
            cost[i] += min(c1, c2)

    from collections import defaultdict
    adj = defaultdict(set)
    for i in range(N):
        for j in range(M):
            if grid[i][j] != -1:
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] != -1 and grid[nx][ny] != grid[i][j]:
                            adj[grid[i][j]].add(grid[nx][ny])
                            adj[grid[nx][j]].add(grid[i][j])

    from collections import deque
    dp = [0]*len(rooms)
    for i in range(len(rooms)):
        dp[i] = cost[i]

    for u in range(len(rooms)):
        for v in adj[u]:
            if v > u:
                dp[v] = min(dp[v], dp[u] + cost[v] - cost[u])

    total = sum(dp)
    for i in range(len(rooms)):
        for j in adj[i]:
            if j > i:
                total += K * len(adj[i] & adj[j])

    print(total)

if __name__ == '__main__':
    main()