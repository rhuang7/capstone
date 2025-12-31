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
    x = 0
    y = 0
    
    # Precompute the sum of distances for each position
    # We'll use prefix sums for each dimension
    # For each step, we'll calculate the sum of |x - xi| and |y - yi|
    # We'll precompute the prefix sums for x and y coordinates of catchers
    
    # Sort catchers by x and y to compute prefix sums
    catchers.sort()
    sorted_x = [x for x, y in catchers]
    sorted_y = [y for x, y in catchers]
    
    # Compute prefix sums for x and y
    prefix_x = [0] * (N + 1)
    prefix_y = [0] * (N + 1)
    
    for i in range(N):
        prefix_x[i + 1] = prefix_x[i] + sorted_x[i]
        prefix_y[i + 1] = prefix_y[i] + sorted_y[i]
    
    # Function to compute sum of absolute differences
    def compute_sum(x_val, y_val):
        sum_x = 0
        sum_y = 0
        for i in range(N):
            dx = abs(x_val - sorted_x[i])
            sum_x += dx
            dy = abs(y_val - sorted_y[i])
            sum_y += dy
        return sum_x + sum_y
    
    # Now simulate the path
    for move in S:
        if move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        
        # Compute the sum of distances to all catchers
        total = 0
        for xi, yi in catchers:
            total += abs(x - xi) + abs(y - yi)
        
        print(total)
    
if __name__ == '__main__':
    solve()