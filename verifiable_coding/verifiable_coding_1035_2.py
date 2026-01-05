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
        for r in range(R):
            row = list(map(int, data[idx:idx+C]))
            grid.append(row)
            idx += C
        
        # Dijkstra's algorithm with priority queue
        # Each state is (current_value, x, y, used_tel_pairs)
        # We use a priority queue to always expand the highest value path
        # We use a visited set to avoid revisiting the same state
        # Since N is small (<=9), we can represent used_tel_pairs as a bitmask
        # The maximum number of states is R*C*2^N
        # For R, C up to 1000 and N up to 9, this is 1000*1000*512 = 512,000,000 which is too big
        # So we need a better approach
        
        # Since N is small (<=9), we can use BFS with pruning
        # We can use a dynamic programming approach where dp[k][x][y] is the maximum value achievable
        # with k teleportations used, ending at (x, y)
        # We can initialize dp[0][Sx][Sy] = grid[Sx][Sy]
        # Then for each k from 0 to N, and for each cell (x, y), we try all possible teleportations
        # and update dp[k+1][new_x][new_y] = max(dp[k+1][new_x][new_y], dp[k][x][y] + grid[new_x][new_y])
        # Finally, the answer is the maximum value in dp[0..N][x][y]
        
        # Since R and C are up to 1000, and N is up to 9, this is feasible
        # We use a 3D array: dp[k][x][y]
        # But since N is small, we can use a list of 2D arrays
        
        # Initialize dp
        dp = [ [[-1 for _ in range(C)] for _ in range(R)] for _ in range(N+1) ]
        dp[0][Sx][Sy] = grid[Sx][Sy]
        
        for k in range(N):
            for x in range(R):
                for y in range(C):
                    if dp[k][x][y] == -1:
                        continue
                    # Try all possible teleportations
                    for i in range(N):
                        if (k & (1 << i)) != 0:
                            continue
                        dx_i = dx[i]
                        dy_i = dy[i]
                        # Try all possible directions
                        for dx_dir in [-dx_i, dx_i]:
                            for dy_dir in [-dy_i, dy_i]:
                                nx = x + dx_dir
                                ny = y + dy_dir
                                if 0 <= nx < R and 0 <= ny < C:
                                    new_val = dp[k][x][y] + grid[nx][ny]
                                    if new_val > dp[k+1][nx][ny]:
                                        dp[k+1][nx][ny] = new_val
        
        # Find the maximum value in dp[0..N]
        max_val = 0
        for k in range(N+1):
            for x in range(R):
                for y in range(C):
                    if dp[k][x][y] > max_val:
                        max_val = dp[k][x][y]
        results.append(str(max_val))
    
    print('\n'.join(results))