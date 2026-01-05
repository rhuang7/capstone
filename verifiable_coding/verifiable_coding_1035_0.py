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
        
        dx = list(map(int, data[idx:idx+N]))
        idx += N
        dy = list(map(int, data[idx:idx+N]))
        idx += N
        
        grid = []
        for i in range(R):
            row = list(map(int, data[idx:idx+C]))
            grid.append(row)
            idx += C
        
        from collections import deque
        
        # Dijkstra's algorithm with priority queue
        # We need to track the maximum value we can get to each cell with a certain number of teleportations used
        # Since N is small (up to 9), we can use a 3D array: dp[teleports_used][x][y]
        # But since R and C can be up to 1000, a 3D array is not feasible
        # So we use a dictionary to track the best value for each (x, y, teleports_used)
        # We also use a priority queue to always expand the path with the highest value first
        
        # We use a priority queue (max-heap) to always expand the path with the highest value first
        # Each element in the queue is (-value, teleports_used, x, y)
        # We use a dictionary to track the best value for each (x, y, teleports_used)
        # We also use a visited set to avoid revisiting the same state
        
        from heapq import heappush, heappop
        
        max_value = 0
        heap = []
        heappush(heap, (0, 0, Sx, Sy))  # (negative value, teleports_used, x, y)
        visited = set()
        visited.add((0, Sx, Sy))
        grid_value = grid[Sx][Sy]
        
        while heap:
            neg_val, teleports_used, x, y = heappop(heap)
            val = -neg_val
            if val > max_value:
                max_value = val
            # Check if we have used all teleports
            if teleports_used == N:
                continue
            # Try using a teleport
            for i in range(N):
                dx_i = dx[i]
                dy_i = dy[i]
                # Teleport can be in any direction
                for dx_sign in [-1, 1]:
                    for dy_sign in [-1, 1]:
                        new_x = x + dx_sign * dx_i
                        new_y = y + dy_sign * dy_i
                        if 0 <= new_x < R and 0 <= new_y < C:
                            new_val = val + grid[new_x][new_y]
                            state = (teleports_used + 1, new_x, new_y)
                            if state not in visited or new_val > visited.get(state, -1):
                                visited.add(state)
                                heappush(heap, (-new_val, teleports_used + 1, new_x, new_y))
            # Also consider not using a teleport
            # This is already handled by the loop, as we can choose to not use any teleport
            # So we just continue with the same teleports_used and same position
        
        results.append(str(max_value))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()