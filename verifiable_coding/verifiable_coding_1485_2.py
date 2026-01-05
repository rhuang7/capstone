import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        grid = []
        for _ in range(N):
            row = data[idx]
            grid.append(row)
            idx += 1
        
        # Calculate initial counts
        left = 0
        right = 0
        for row in grid:
            for i in range(N//2):
                if row[i] == '1':
                    left += 1
                if row[N-1-i] == '1':
                    right += 1
        
        # Calculate the initial difference
        diff = abs(left - right)
        results.append(diff)
        
        # Try reversing each row
        for i in range(N):
            new_left = left
            new_right = right
            for j in range(N//2):
                if grid[i][j] == '1':
                    new_left -= 1
                if grid[i][N-1-j] == '1':
                    new_right -= 1
            for j in range(N//2):
                if grid[i][N-1-j] == '1':
                    new_left += 1
                if grid[i][j] == '1':
                    new_right += 1
            current_diff = abs(new_left - new_right)
            if current_diff < diff:
                diff = current_diff
        
        results[-1] = diff
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()