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
        
        # Dijkstra's algorithm with priority queue
        from heapq import heappush, heappop
        
        # Each state is (current_value, x, y, used_tels)
        # We use a priority queue to always expand the highest value path
        # We use a dictionary to keep track of the maximum value for each (x, y, used_tels)
        max_values = {}
        heap = []
        heappush(heap, (-grid[Sx][Sy], Sx, Sy, 0))
        max_values[(Sx, Sy, 0)] = grid[Sx][Sy]
        
        while heap:
            neg_val, x, y, used = heappop(heap)
            val = -neg_val
            if (x, y, used) in max_values and max_values[(x, y, used)] > val:
                continue
            if used == N:
                results.append(val)
                break
            # Try using a tel-pair
            for i in range(N):
                if used > i:
                    dx_i = dx[i]
                    dy_i = dy[i]
                    new_x = x + dx_i
                    new_y = y + dy_i
                    if 0 <= new_x < R and 0 <= new_y < C:
                        new_val = val + grid[new_x][new_y]
                        key = (new_x, new_y, used + 1)
                        if key not in max_values or new_val > max_values[key]:
                            max_values[key] = new_val
                            heappush(heap, (-new_val, new_x, new_y, used + 1))
            # Try not using a tel-pair
            key = (x, y, used)
            if key not in max_values or val > max_values[key]:
                max_values[key] = val
                heappush(heap, (-val, x, y, used))
        
        # If we didn't break out of the loop, then we have to check all possibilities
        if len(results) == 0:
            max_val = 0
            for key in max_values:
                if max_values[key] > max_val:
                    max_val = max_values[key]
            results.append(max_val)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()