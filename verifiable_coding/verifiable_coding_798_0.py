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
    
    # Preprocess safe cells
    safe = [[False] * N for _ in range(N)]
    for x, y, k in charms:
        for dx in range(-k, k + 1):
            for dy in range(-k, k + 1):
                if abs(dx) + abs(dy) <= k:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        safe[nx][ny] = True
    
    # Check if (0,0) and (N-1,N-1) are safe
    if not safe[0][0] or not safe[N-1][N-1]:
        print("NO")
        return
    
    # Dijkstra's algorithm to find max berries
    # We use a priority queue with (current_berries, x, y)
    # Since we want to maximize berries, we use a max-heap
    # But Python's heapq is a min-heap, so we store negative values
    # We also need to track visited cells with the maximum berries found so far
    from collections import defaultdict
    import heapq
    
    max_berries = [[-float('inf')] * N for _ in range(N)]
    max_berries[0][0] = grid[0][0]
    heap = [(-grid[0][0], 0, 0)]
    
    directions = [(0, 1), (1, 0)]
    
    while heap:
        curr = -heapq.heappop(heap)
        x, y = heapq.heappop(heap)
        x = -x
        y = -y
        if x == N-1 and y == N-1:
            break
        if curr < max_berries[x][y]:
            continue
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and safe[nx][ny]:
                new_berries = curr + grid[nx][ny]
                if new_berries > max_berries[nx][ny]:
                    max_berries[nx][ny] = new_berries
                    heapq.heappush(heap, (-new_berries, nx, ny))
    
    if max_berries[N-1][N-1] == -float('inf'):
        print("NO")
    else:
        print("YES")
        print(-max_berries[N-1][N-1])