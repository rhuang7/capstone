import sys
import math

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
        for _ in range(R):
            row = list(map(int, data[idx:idx+C]))
            grid.append(row)
            idx += C
        
        # Precompute all possible teleportations
        teleports = []
        for dx in dx_list:
            for dy in dy_list:
                teleports.append((dx, dy))
        
        # Dijkstra's algorithm with priority queue
        from heapq import heappush, heappop
        import collections
        
        # Each state is (current_value, x, y, used_teleports)
        # We use a max-heap (negated for min-heap)
        heap = [(-grid[Sx][Sy], Sx, Sy, 0)]
        visited = set()
        max_value = 0
        
        while heap:
            current_val, x, y, used = heappop(heap)
            current_val = -current_val
            if (x, y, used) in visited:
                continue
            visited.add((x, y, used))
            max_value = max(max_value, current_val)
            
            # If we have used all teleportations, we can't move further
            if used == N:
                continue
            
            # Try using the next teleportation
            for i in range(used, N):
                dx = dx_list[i]
                dy = dy_list[i]
                # Teleport from (x, y) to (x + dx, y + dy) or (x - dx, y + dy)
                # or (x + dx, y - dy) or (x - dx, y - dy)
                for dx2, dy2 in [(dx, dy), (-dx, dy), (dx, -dy), (-dx, -dy)]:
                    nx = x + dx2
                    ny = y + dy2
                    if 0 <= nx < R and 0 <= ny < C:
                        new_val = current_val + grid[nx][ny]
                        heappush(heap, (-new_val, nx, ny, used + 1))
        
        results.append(str(max_value))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()