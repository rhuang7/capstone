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

    # Check if there's any path from (0,0) to (N-1,N-1)
    # Using BFS to check if there's any path
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            break
        for dx, dy in [(0, 1), (1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and safe[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    if not visited[N-1][N-1]:
        print("NO")
        return

    # Dijkstra's algorithm to find max berries
    # Use a priority queue with (current_berries, x, y)
    # We want to maximize the berries, so we use a max-heap
    # Since Python's heapq is a min-heap, we store negative values
    heap = [(-grid[0][0], 0, 0)]
    dist = [[-float('inf')]*N for _ in range(N)]
    dist[0][0] = grid[0][0]
    while heap:
        curr = -heapq.heappop(heap)
        x, y = curr[1], curr[2]
        if x == N-1 and y == N-1:
            break
        for dx, dy in [(0, 1), (1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and safe[nx][ny]:
                if dist[nx][ny] < dist[x][y] + grid[nx][ny]:
                    dist[nx][ny] = dist[x][y] + grid[nx][ny]
                    heapq.heappush(heap, (-dist[nx][ny], nx, ny))

    print("YES")
    print(dist[N-1][N-1])