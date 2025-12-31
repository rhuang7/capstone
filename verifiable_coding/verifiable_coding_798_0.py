import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    grid = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        grid.append(row)
        idx += N

    charms = []
    for _ in range(M):
        x = int(data[idx]) - 1
        idx += 1
        y = int(data[idx]) - 1
        idx += 1
        k = int(data[idx])
        idx += 1
        charms.append((x, y, k))

    # Precompute safe cells
    safe = [[False]*N for _ in range(N)]
    for x, y, k in charms:
        for dx in range(-k, k+1):
            for dy in range(-k, k+1):
                if abs(dx) + abs(dy) <= k:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        safe[nx][ny] = True

    # Dijkstra's algorithm to find max berries
    from collections import deque

    # Create a priority queue for Dijkstra's
    # We use a max-heap (using negative values)
    # Each element is (-berry_count, x, y)
    # We also track the maximum berries collected to reach each cell
    max_berry = [[-float('inf')]*N for _ in range(N)]
    max_berry[0][0] = grid[0][0]
    pq = []
    heapq.heappush(pq, (-grid[0][0], 0, 0))

    # Directions: right, down
    dirs = [(0, 1), (1, 0)]

    while pq:
        curr = heapq.heappop(pq)
        curr_berry = -curr[0]
        x, y = curr[1], curr[2]

        if x == N-1 and y == N-1:
            break

        if not safe[x][y]:
            continue

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and safe[nx][ny]:
                new_berry = curr_berry + grid[nx][ny]
                if new_berry > max_berry[nx][ny]:
                    max_berry[nx][ny] = new_berry
                    heapq.heappush(pq, (-new_berry, nx, ny))

    if max_berry[N-1][N-1] == -float('inf'):
        print("NO")
    else:
        print("YES")
        print(max_berry[N-1][N-1])