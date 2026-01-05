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
    
    # Precompute prefix sums for x and y coordinates
    # For each position on Tuzik's path, compute sum of |x - x_i| and |y - y_i|
    # For each position, sum over all catchers
    
    # Initialize current position
    x = 0
    y = 0
    
    # Precompute sorted x and y coordinates of catchers
    sorted_x = sorted(catchers_x)
    sorted_y = sorted(catchers_y)
    
    # Precompute prefix sums for x and y
    prefix_x = [0] * (N + 1)
    prefix_y = [0] * (N + 1)
    for i in range(N):
        prefix_x[i + 1] = prefix_x[i] + sorted_x[i]
        prefix_y[i + 1] = prefix_y[i] + sorted_y[i]
    
    # Function to compute sum of absolute differences
    def compute_sum(sorted_list, prefix_sum):
        total = 0
        for i in range(N):
            total += abs(sorted_list[i] - sorted_list[0]) * (i + 1) + abs(sorted_list[i] - sorted_list[-1]) * (N - i)
        return total
    
    # Precompute the sum of absolute differences for x and y
    sum_x = compute_sum(sorted_x, prefix_x)
    sum_y = compute_sum(sorted_y, prefix_y)
    
    # Now simulate Tuzik's path
    # We will keep track of the current position and compute the sum for each step
    # We will use the sorted lists and prefix sums to compute the sum efficiently
    
    # Precompute the sum for each position on the path
    # We will use a prefix sum approach for x and y coordinates
    # We will keep track of the current x and y coordinates
    # For each step, we will compute the sum of distances to all catchers
    
    # Initialize current x and y
    curr_x = 0
    curr_y = 0
    
    # Precompute the prefix sums for x and y
    # We will use binary search to find the number of catchers with x <= curr_x and x >= curr_x
    # This allows us to compute the sum of absolute differences efficiently
    
    # Precompute the sorted x and y coordinates
    sorted_x = sorted(catchers_x)
    sorted_y = sorted(catchers_y)
    
    # Precompute prefix sums for x and y
    prefix_x = [0] * (N + 1)
    prefix_y = [0] * (N + 1)
    for i in range(N):
        prefix_x[i + 1] = prefix_x[i] + sorted_x[i]
        prefix_y[i + 1] = prefix_y[i] + sorted_y[i]
    
    # Function to compute the sum of absolute differences for a given x and y
    def compute_sum(x, y):
        # Compute sum for x
        # Find the number of catchers with x <= current x
        # Using binary search
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if sorted_x[mid] <= x:
                left = mid + 1
            else:
                right = mid
        cnt_less = left
        sum_x = x * cnt_less - prefix_x[cnt_less]
        sum_x += (prefix_x[N] - prefix_x[cnt_less]) - x * (N - cnt_less)
        
        # Compute sum for y
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if sorted_y[mid] <= y:
                left = mid + 1
            else:
                right = mid
        cnt_less = left
        sum_y = y * cnt_less - prefix_y[cnt_less]
        sum_y += (prefix_y[N] - prefix_y[cnt_less]) - y * (N - cnt_less)
        
        return sum_x + sum_y
    
    # Now simulate the path
    for c in S:
        if c == 'R':
            curr_x += 1
        elif c == 'L':
            curr_x -= 1
        elif c == 'U':
            curr_y += 1
        elif c == 'D':
            curr_y -= 1
        
        # Compute the sum for the current position
        # Exclude the starting position (0, 0)
        if (curr_x, curr_y) != (0, 0):
            print(compute_sum(curr_x, curr_y))