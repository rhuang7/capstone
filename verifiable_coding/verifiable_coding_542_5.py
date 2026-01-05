import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        grid = []
        for _ in range(N):
            grid.append(input[idx])
            idx += 1
        
        count = 0
        
        for i in range(N - 1):
            for j in range(M - 1):
                # Check 2x2 square starting at (i, j)
                top_left = grid[i][j]
                top_right = grid[i][j+1]
                bottom_left = grid[i+1][j]
                bottom_right = grid[i+1][j+1]
                
                if top_left == top_right == bottom_left == bottom_right:
                    count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()