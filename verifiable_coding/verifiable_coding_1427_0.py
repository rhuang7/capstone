import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    catchers = []
    for _ in range(N):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        catchers.append((x, y))
    
    S = data[idx]
    
    # Precompute all catcher positions
    catchers_x = [x for x, y in catchers]
    catchers_y = [y for x, y in catchers]
    
    # Initialize current position
    x, y = 0, 0
    # Initialize cumulative sum for each direction
    dx_sum = 0
    dy_sum = 0
    
    for c in S:
        if c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        
        # Compute distance to each catcher
        total = 0
        for i in range(N):
            total += abs(x - catchers_x[i]) + abs(y - catchers_y[i])
        
        print(total)
    
if __name__ == '__main__':
    solve()