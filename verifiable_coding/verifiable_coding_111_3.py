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
        toggles = 0
        for i in range(0, new_n, k):
            for j in range(0, new_m, k):
                block = []
                for x in range(i, i + k):
                    block.append(padded[x][j:j + k])
                # Find the value that appears most in the block
                cnt0 = 0
                cnt1 = 0
                for row in block:
                    for c in row:
                        if c == '0':
                            cnt0 += 1
                        else:
                            cnt1 += 1
                if cnt0 > cnt1:
                    target = '0'
                else:
                    target = '1'
                # Toggle all pixels in the block to target
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if padded[x][y] != target:
                            toggles += 1
        min_toggles = min(min_toggles, toggles)
    
    print(min_toggles)