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
        # Calculate new dimensions after padding
        new_n = ((n + k - 1) // k) * k
        new_m = ((m + k - 1) // k) * k
        
        # Create padded grid
        padded = []
        for i in range(n):
            padded.append(grid[i] + '0' * (new_m - m))
        for i in range(n, new_n):
            padded.append('0' * new_m)
        
        # Process each block
        total = 0
        for i in range(0, new_n, k):
            for j in range(0, new_m, k):
                block = []
                for x in range(i, i + k):
                    block.extend(padded[x][j:j + k])
                # Count the number of 0s and 1s in the block
                cnt0 = block.count('0')
                cnt1 = block.count('1')
                # Toggle to make all same
                total += min(cnt0, cnt1)
        
        min_toggles = min(min_toggles, total)
    
    print(min_toggles)