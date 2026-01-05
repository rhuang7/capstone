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
            for i in range(N // 2):
                if row[i] == '1':
                    left += 1
                if row[N - 1 - i] == '1':
                    right += 1
        
        # Try reversing each row
        min_diff = abs(left - right)
        for i in range(N):
            # Create reversed row
            reversed_row = []
            for j in range(N // 2):
                reversed_row.append(grid[i][N - 1 - j])
            for j in range(N // 2):
                reversed_row.append(grid[i][j])
            
            # Calculate new counts
            new_left = left
            new_right = right
            for j in range(N // 2):
                if reversed_row[j] == '1':
                    new_left += 1
                if reversed_row[N - 1 - j] == '1':
                    new_right += 1
            
            current_diff = abs(new_left - new_right)
            if current_diff < min_diff:
                min_diff = current_diff
        
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()