import sys
import math

MOD = 21945

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        N = int(data[idx])
        idx += 1
        
        grid = []
        for _ in range(8):
            grid.append(data[idx])
            idx += 1
        
        # Determine how many times the napkin was unfolded
        # Original size is 2^n x 2^n, after n-3 folds it becomes 8x8
        # So 2^n = 8 * 2^(n-3) => 2^n = 2^(n-3 + 3) => 2^n = 2^n, which is always true
        # So we can directly compute the number of folds
        # The number of folds is (n - 3)
        # Each fold doubles the number of regions
        # But we need to account for the way the folds are done
        
        # The original napkin is 2^n x 2^n
        # After each fold, the size is halved
        # After n-3 folds, the size is 8x8
        # So 2^n / 2^(n-3) = 8 => 2^3 = 8, which is correct
        
        # The number of regions is 2^(number of folds) * number of regions in 8x8
        # But the way the folds are done is important
        
        # Each fold is a vertical and horizontal fold
        # The first fold is vertical, then horizontal, then vertical, etc.
        # Each fold doubles the number of regions
        
        # So the number of regions is 2^(number of folds) * number of regions in 8x8
        
        # But the way the folds are done is such that each fold doubles the number of regions
        # So the number of regions in the unfolded napkin is 2^(number of folds) * number of regions in 8x8
        
        # So we need to find the number of regions in the 8x8 grid
        
        # Count the number of regions in the 8x8 grid
        # We can do this with a BFS or DFS
        
        # Initialize visited matrix
        visited = [[False for _ in range(8)] for _ in range(8)]
        regions = 0
        
        # Directions for BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(8):
            for j in range(8):
                if grid[i][j] == '1' and not visited[i][j]:
                    regions += 1
                    # BFS
                    queue = [(i, j)]
                    visited[i][j] = True
                    while queue:
                        x, y = queue.pop(0)
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny] and grid[nx][ny] == '1':
                                visited[nx][ny] = True
                                queue.append((nx, ny))
        
        # Number of folds is (n - 3)
        # Each fold doubles the number of regions
        # So the total number of regions is regions * 2^(n-3)
        # But we need to handle the case where n-3 is negative
        # Since n >= 3, n-3 >= 0
        
        # Compute 2^(n-3) mod MOD
        power = pow(2, N - 3, MOD)
        total = (regions * power) % MOD
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()