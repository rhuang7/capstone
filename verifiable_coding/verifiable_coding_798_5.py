import sys
import math

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
    
    # Create a grid of safe cells
    safe = [[False]*N for _ in range(N)]
    for x, y, k in charms:
        for dx in range(-k, k+1):
            for dy in range(-k, k+1):
                if abs(dx) + abs(dy) <= k:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        safe[nx][ny] = True
    
    # Check if (0,0) and (N-1, N-1) are safe
    if not safe[0][0] or not safe[N-1][N-1]:
        print("NO")
        return
    
    # Use Dijkstra's algorithm to find maximum berries
    from heapq import heappush, heappop
    
    # Priority queue: (current_berries, x, y)
    pq = []
    heappush(pq, (0, 0, 0))
    
    # Distance matrix
    dist = [[-float('inf')]*N for _ in range(N)]
    dist[0][0] = grid[0][0]
    
    while pq:
        curr, x, y = heappop(pq)
        if x == N-1 and y == N-1:
            break
        if curr < dist[x][y]:
            continue
        for dx, dy in [(0, 1), (1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and safe[nx][ny]:
                new_dist = curr + grid[nx][ny]
                if new_dist > dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
    
    if dist[N-1][N-1] == -float('inf'):
        print("NO")
    else:
        print("YES")
        print(dist[N-1][N-1])

if __name__ == '__main__':
    solve()