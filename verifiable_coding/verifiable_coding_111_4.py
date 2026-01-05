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
        new_n = ((n - 1) // k + 1) * k
        new_m = ((m - 1) // k + 1) * k
        
        # Create padded grid
        padded = []
        for i in range(n):
            row = grid[i]
            padded_row = row.ljust(new_m, '0')
            padded.append(padded_row)
        for i in range(n, new_n):
            padded.append('0' * new_m)
        
        # Calculate toggles for this k
        toggles = 0
        for i in range(0, new_n, k):
            for j in range(0, new_m, k):
                block = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        block.append(padded[x][y])
                target = block[0]
                for val in block:
                    if val != target:
                        toggles += 1
        min_toggles = min(min_toggles, toggles)
    
    print(min_toggles)