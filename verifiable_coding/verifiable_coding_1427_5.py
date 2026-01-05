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
    
    # Precompute the sum of x and y coordinates of catchers
    sum_x = sum(catchers_x)
    sum_y = sum(catchers_y)
    
    # Initialize current position
    x, y = 0, 0
    
    # Process each step of the path
    for c in S:
        # Update position
        if c == 'D':
            y -= 1
        elif c == 'U':
            y += 1
        elif c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        
        # Calculate Manhattan distance to all catchers
        total = 0
        for i in range(N):
            dx = abs(x - catchers_x[i])
            dy = abs(y - catchers_y[i])
            total += dx + dy
        
        # Output the total distance
        print(total)

if __name__ == '__main__':
    solve()