import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        N = int(data[idx+2])
        idx += 3
        Sx = int(data[idx])
        Sy = int(data[idx+1])
        idx += 2
        dxs = list(map(int, data[idx:idx+N]))
        idx += N
        dys = list(map(int, data[idx:idx+N]))
        idx += N
        grid = []
        for r in range(R):
            row = list(map(int, data[idx:idx+C]))
            grid.append(row)
            idx += C
        
        # Dijkstra's algorithm with priority queue
        # Each state is (current_value, x, y, used_tels)
        # We use a priority queue to find the maximum value path
        # Since N is small (<=9), we can use a state (x, y, used_tels)
        # where used_tels is a bitmask of used tel-pairs
        
        # Initialize the priority queue
        # Start at (Sx, Sy) with value grid[Sx][Sy], used_tels=0
        pq = []
        heapq.heappush(pq, (-grid[Sx][Sy], Sx, Sy, 0))
        
        # Visited array: (x, y, used_tels) -> max value
        visited = {}
        
        while pq:
            neg_val, x, y, used = heapq.heappop(pq)
            val = -neg_val
            key = (x, y, used)
            if key in visited and visited[key] >= val:
                continue
            visited[key] = val
            
            # Try using each tel-pair if not used
            for i in range(N):
                if not (used & (1 << i)):
                    dx = dxs[i]
                    dy = dys[i]
                    # Possible moves: (x + dx, y + dy), (x - dx, y + dy), (x + dx, y - dy), (x - dx, y - dy)
                    for dx2, dy2 in [(dx, dy), (-dx, dy), (dx, -dy), (-dx, -dy)]:
                        nx = x + dx2
                        ny = y + dy2
                        if 0 <= nx < R and 0 <= ny < C:
                            new_val = val + grid[nx][ny]
                            new_used = used | (1 << i)
                            new_key = (nx, ny, new_used)
                            if new_key not in visited or visited[new_key] < new_val:
                                heapq.heappush(pq, (-new_val, nx, ny, new_used))
            
            # Also consider not using any tel-pair (stay in current cell)
            # This is already handled by the initial state, but we can add it again
            # to ensure that we can revisit the same cell with the same used_tels
            # but with higher value
            new_key = (x, y, used)
            if new_key not in visited or visited[new_key] < val:
                heapq.heappush(pq, (-val, x, y, used))
        
        # Find the maximum value among all visited states
        max_val = 0
        for key in visited:
            if visited[key] > max_val:
                max_val = visited[key]
        results.append(str(max_val))
    
    print('\n'.join(results))