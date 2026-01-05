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
            left += row[:N//2].count('1')
            right += row[N//2:].count('1')
        
        min_diff = abs(left - right)
        
        # Try reversing each row
        for i in range(N):
            # Create a new row by reversing the row
            new_row = grid[i][::-1]
            # Calculate new counts
            new_left = left - grid[i][:N//2].count('1') + new_row[:N//2].count('1')
            new_right = right - grid[i][N//2:].count('1') + new_row[N//2:].count('1')
            current_diff = abs(new_left - new_right)
            if current_diff < min_diff:
                min_diff = current_diff
        
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()