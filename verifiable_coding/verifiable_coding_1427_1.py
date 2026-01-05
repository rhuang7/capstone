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
    
    # Initial position
    x, y = 0, 0
    # We'll keep track of the sum of distances for each position
    # We'll use prefix sums to compute the total distance efficiently
    
    # For each direction, we'll compute the prefix sum of x and y coordinates
    # Then for each position, we can compute the total distance by summing over all catchers
    
    # Precompute prefix sums for x and y
    prefix_x = [0] * (M + 1)
    prefix_y = [0] * (M + 1)
    
    for i in range(M):
        dx = 0
        dy = 0
        if S[i] == 'R':
            dx = 1
        elif S[i] == 'L':
            dx = -1
        elif S[i] == 'U':
            dy = 1
        elif S[i] == 'D':
            dy = -1
        x += dx
        y += dy
        prefix_x[i + 1] = prefix_x[i] + x
        prefix_y[i + 1] = prefix_y[i] + y
    
    # Compute the total distance for each position
    # We'll use the fact that distance is Manhattan distance
    # For each position (x, y), total distance is sum(|x - xi| + |y - yi| for all catchers)
    # Which can be rewritten as sum(|x - xi|) + sum(|y - yi|)
    
    # Precompute prefix sums for x and y of catchers
    prefix_catch_x = [0] * (N + 1)
    prefix_catch_y = [0] * (N + 1)
    
    for i in range(N):
        prefix_catch_x[i + 1] = prefix_catch_x[i] + catchers_x[i]
        prefix_catch_y[i + 1] = prefix_catch_y[i] + catchers_y[i]
    
    # For each position, compute the total distance
    for i in range(1, M):
        x = prefix_x[i]
        y = prefix_y[i]
        # Compute sum of |x - xi| for all catchers
        # This can be done using prefix sums
        # Sort catchers by x and y
        # But since N is large, we need an efficient way
        # We can compute it using the formula for sum of absolute differences
        # Let's sort the catchers by x and y
        # But since we have to do this for each position, it's better to precompute sorted lists
        # So we sort the catchers by x and y
        
        # Pre-sort catchers by x and y
        sorted_x = sorted(catchers_x)
        sorted_y = sorted(catchers_y)
        
        # Compute sum of |x - xi| for all catchers
        # Using the formula for sorted array
        # Let's compute it for each position
        # For x
        # Find the index where x would be inserted in sorted_x
        # This is the number of elements <= x
        # Then sum = x * idx - prefix_catch_x[idx] + (prefix_catch_x[N] - prefix_catch_x[idx] - x * (N - idx))
        # Similarly for y
        
        # Compute sum of |x - xi|
        # Using binary search to find the insertion point
        # For x
        from bisect import bisect_right
        idx_x = bisect_right(sorted_x, x)
        sum_x = x * idx_x - prefix_catch_x[idx_x] + (prefix_catch_x[N] - prefix_catch_x[idx_x] - x * (N - idx_x))
        
        # For y
        idx_y = bisect_right(sorted_y, y)
        sum_y = y * idx_y - prefix_catch_y[idx_y] + (prefix_catch_y[N] - prefix_catch_y[idx_y] - y * (N - idx_y))
        
        total = sum_x + sum_y
        print(total)
        
solve()