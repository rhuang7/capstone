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
        dx_list = list(map(int, data[idx:idx+N]))
        idx += N
        dy_list = list(map(int, data[idx:idx+N]))
        idx += N
        grid = []
        for r in range(R):
            row = list(map(int, data[idx:idx+C]))
            grid.append(row)
            idx += C
        
        # Dijkstra's algorithm with priority queue
        # Each state is (current_value, x, y, used_tels)
        # We use a priority queue to find the maximum value path
        # Since N is small (up to 9), we can use a 3D array for visited
        # visited[used_tels][x][y] = max_value
        # Since R and C can be up to 1000, a 3D array is not feasible
        # So we use a dictionary to store the best value for each (x, y, used_tels)
        from collections import defaultdict
        import heapq
        
        max_value = 0
        # Priority queue: (current_value, x, y, used_tels)
        pq = [(grid[Sx][Sy], Sx, Sy, 0)]
        # Dictionary to store the best value for each (x, y, used_tels)
        visited = dict()
        visited[(Sx, Sy, 0)] = grid[Sx][Sy]
        
        while pq:
            current_val, x, y, used = heapq.heappop(pq)
            current_val = -current_val  # Because we use a max heap via negation
            
            # Check if this is the best value for (x, y, used)
            if (x, y, used) in visited and visited[(x, y, used)] > current_val:
                continue
            
            # If we have used all tel-pairs, we can't use any more
            if used == N:
                max_value = max(max_value, current_val)
                continue
            
            # Try using the next tel-pair
            for i in range(used, N):
                dx = dx_list[i]
                dy = dy_list[i]
                # Generate all possible cells reachable by this tel-pair
                for dx2 in [-dx, dx]:
                    for dy2 in [-dy, dy]:
                        nx = x + dx2
                        ny = y + dy2
                        if 0 <= nx < R and 0 <= ny < C:
                            new_val = current_val + grid[nx][ny]
                            state = (nx, ny, i + 1)
                            if state not in visited or new_val > visited[state]:
                                visited[state] = new_val
                                heapq.heappush(pq, (-new_val, nx, ny, i + 1))
            
            # Also consider not using the next tel-pair
            # This is already handled by the loop, as we can choose to not use it
            # So we just continue with the same used count
            
            max_value = max(max_value, current_val)
        
        results.append(str(max_value))
    
    print('\n'.join(results))