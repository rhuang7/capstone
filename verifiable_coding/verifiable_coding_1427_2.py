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
    
    # Precompute the number of catchers
    cnt = N
    
    # Initialize current position
    x = 0
    y = 0
    
    # Process each step in the path
    for i in range(M):
        c = S[i]
        if c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        
        # Calculate the sum of Manhattan distances to all catchers
        total = 0
        for j in range(N):
            dx = abs(x - catchers_x[j])
            dy = abs(y - catchers_y[j])
            total += dx + dy
        
        print(total)
    
if __name__ == '__main__':
    solve()