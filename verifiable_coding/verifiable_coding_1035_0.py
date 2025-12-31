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
        # Each state is (total_value, x, y, used_pairs)
        # Since N is small (<=9), we can represent used_pairs as a bitmask
        # We use a priority queue to find the maximum value path
        # We use a dictionary to keep track of the maximum value for each (x, y, used_pairs)
        from collections import defaultdict
        import heapq
        
        max_value = 0
        heap = []
        heapq.heappush(heap, (-grid[Sx][Sy], Sx, Sy, 0))  # Use negative for max-heap
        visited = defaultdict(lambda: defaultdict(lambda: -1))
        visited[Sx][Sy][0] = grid[Sx][Sy]
        
        while heap:
            neg_total, x, y, used = heapq.heappop(heap)
            total = -neg_total
            if total > max_value:
                max_value = total
            if used == N:
                continue
            # Try using the next tel-pair
            for i in range(used, N):
                dx = dx_list[i]
                dy = dy_list[i]
                # Try all possible cells reachable by this tel-pair
                for dx2 in [-dx, dx]:
                    for dy2 in [-dy, dy]:
                        nx = x + dx2
                        ny = y + dy2
                        if 0 <= nx < R and 0 <= ny < C:
                            new_total = total + grid[nx][ny]
                            new_used = used + 1
                            if new_total > visited[nx][ny][new_used]:
                                visited[nx][ny][new_used] = new_total
                                heapq.heappush(heap, (-new_total, nx, ny, new_used))
            # Also consider staying in the same cell (no teleport)
            if total > visited[x][y][used]:
                visited[x][y][used] = total
                heapq.heappush(heap, (-total, x, y, used))
        
        results.append(str(max_value))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()