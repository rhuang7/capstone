import sys
import math

MOD = 21945

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        N = int(input[idx])
        idx += 1
        grid = []
        for _ in range(8):
            grid.append(input[idx])
            idx += 1
        # Determine how many times the napkin was unfolded
        # Original size is 2^n x 2^n, final size is 8x8
        # So 2^n = 8 => n = 3
        # So the number of folds is n-3 = 0
        # So the napkin was not unfolded
        # So the grid is already the unfolded one
        # So we just need to count the number of connected regions in the grid
        # Use BFS to count connected regions
        visited = [[False]*8 for _ in range(8)]
        count = 0
        for i in range(8):
            for j in range(8):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    # BFS
                    q = [(i, j)]
                    visited[i][j] = True
                    while q:
                        x, y = q.pop(0)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 8 and 0 <= ny < 8:
                                if grid[nx][ny] == '1' and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))
        print(count % MOD)

if __name__ == '__main__':
    solve()