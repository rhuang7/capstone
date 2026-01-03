import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    grid = data[2:]
    
    min_toggles = float('inf')
    
    for k in range(2, min(n, m) + 1):
        # Calculate the padded dimensions
        padded_n = ((n + k - 1) // k) * k
        padded_m = ((m + k - 1) // k) * k
        
        # Create a padded grid
        padded_grid = []
        for i in range(n):
            padded_grid.append(grid[i] + '0' * (padded_m - m))
        for i in range(n, padded_n):
            padded_grid.append('0' * padded_m)
        
        # Split into k x k blocks
        total_toggles = 0
        for i in range(0, padded_n, k):
            for j in range(0, padded_m, k):
                block = []
                for x in range(i, i + k):
                    block.extend(padded_grid[x][j:j + k])
                # Find the target value for the block
                target = block[0]
                for val in block:
                    if val != target:
                        total_toggles += 1
        min_toggles = min(min_toggles, total_toggles)
    
    print(min_toggles)

if __name__ == '__main__':
    solve()