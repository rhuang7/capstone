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
        half = N // 2
        count1 = 0
        count2 = 0
        for row in grid:
            count1 += row[:half].count('1')
            count2 += row[half:].count('1')
        
        min_diff = abs(count1 - count2)
        
        # Try reversing each row
        for i in range(N):
            row = grid[i]
            # Count how many '1's are in the left half and right half of this row
            left = row[:half].count('1')
            right = row[half:].count('1')
            # After reversing, the left and right halves swap
            new_count1 = count1 - left + right
            new_count2 = count2 - right + left
            current_diff = abs(new_count1 - new_count2)
            if current_diff < min_diff:
                min_diff = current_diff
        
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()