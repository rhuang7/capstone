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
        dx = list(map(int, data[idx:idx+N]))
        idx += N
        dy = list(map(int, data[idx:idx+N]))
        idx += N
        grid = []
        for _ in range(R):
            grid.append(list(map(int, data[idx:idx+C])))
            idx += C
        
        # Dijkstra's algorithm with priority queue
        # Each state is (current_value, x, y, used_tel_pairs)
        # We use a priority queue to always expand the path with the highest value
        # We use a visited set to avoid reprocessing the same state
        # Since N is small (up to 9), we can represent used_tel_pairs as a bitmask
        # The maximum number of states is R*C*2^N
        # Since R and C are up to 1000, and N is up to 9, this is manageable
        
        from collections import defaultdict
        import heapq
        
        max_val = 0
        heap = []
        heapq.heappush(heap, (-grid[Sx][Sy], Sx, Sy, 0))  # Use negative for max-heap
        visited = set()
        visited.add((Sx, Sy, 0))
        
        while heap:
            neg_val, x, y, used = heapq.heappop(heap)
            val = -neg_val
            if val > max_val:
                max_val = val
            if used == (1 << N) - 1:
                continue  # All tel-pairs used
            # Try moving to adjacent cells using tel-pairs
            for i in range(N):
                if not (used & (1 << i)):
                    dx_i = dx[i]
                    dy_i = dy[i]
                    # Teleport to (x + dx_i, y + dy_i)
                    nx = x + dx_i
                    ny = y + dy_i
                    if 0 <= nx < R and 0 <= ny < C:
                        new_used = used | (1 << i)
                        new_val = val + grid[nx][ny]
                        if (nx, ny, new_used) not in visited:
                            visited.add((nx, ny, new_used))
                            heapq.heappush(heap, (-new_val, nx, ny, new_used))
                    # Teleport to (x - dx_i, y - dy_i)
                    nx = x - dx_i
                    ny = y - dy_i
                    if 0 <= nx < R and 0 <= ny < C:
                        new_used = used | (1 << i)
                        new_val = val + grid[nx][ny]
                        if (nx, ny, new_used) not in visited:
                            visited.add((nx, ny, new_used))
                            heapq.heappush(heap, (-new_val, nx, ny, new_used))
            # Also consider staying in the same cell (no teleportation)
            # This is already handled by the initial state and the priority queue
            # So no need to add it again
        
        results.append(str(max_val))
    
    print('\n'.join(results))