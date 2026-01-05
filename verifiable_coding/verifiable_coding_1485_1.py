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
        left_count = 0
        right_count = 0
        for row in grid:
            left = row[:N//2]
            right = row[N//2:]
            left_count += left.count('1')
            right_count += right.count('1')
        
        min_diff = abs(left_count - right_count)
        
        # Try reversing each row
        for i in range(N):
            row = grid[i]
            left = row[:N//2]
            right = row[N//2:]
            
            # Count how many 1's are in left and right parts
            left_ones = left.count('1')
            right_ones = right.count('1')
            
            # After reversing, the left part becomes right and vice versa
            new_left_ones = right_ones
            new_right_ones = left_ones
            
            current_diff = abs(new_left_ones - new_right_ones)
            if current_diff < min_diff:
                min_diff = current_diff
        
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()