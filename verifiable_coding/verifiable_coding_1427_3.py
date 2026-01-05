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
    total_x = 0
    total_y = 0
    
    # Precompute the sum of x and y coordinates of catchers
    sum_x = sum(catchers_x)
    sum_y = sum(catchers_y)
    
    # Precompute the number of catchers
    cnt = N
    
    # Process each step in the path
    for c in S:
        # Update current position
        if c == 'D':
            y -= 1
        elif c == 'U':
            y += 1
        elif c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        
        # Compute Manhattan distance to each catcher
        # Distance = |x - x_i| + |y - y_i|
        # Sum over all catchers
        # We can compute this efficiently using prefix sums
        # For x: sum(|x - x_i|) = sum(x - x_i) if x >= all x_i, else sum(x_i - x)
        # Similarly for y
        
        # Compute sum of |x - x_i| for all catchers
        # If x >= all x_i, sum_x = x * cnt - sum_x
        # If x < all x_i, sum_x = sum_x - x * cnt
        # Similarly for y
        
        # Find the number of catchers with x_i <= x
        # We can use binary search for this
        # But since we have to do this for every step, we can precompute sorted x and y
        # Sort catchers by x and y
        catchers_x_sorted = sorted(catchers_x)
        catchers_y_sorted = sorted(catchers_y)
        
        # Binary search for x
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if catchers_x_sorted[mid] <= x:
                left = mid + 1
            else:
                right = mid
        count_x = left
        sum_x_part = x * count_x - sum(catchers_x_sorted[:count_x])
        sum_x_part += sum(catchers_x_sorted[count_x:]) - x * (N - count_x)
        
        # Binary search for y
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if catchers_y_sorted[mid] <= y:
                left = mid + 1
            else:
                right = mid
        count_y = left
        sum_y_part = y * count_y - sum(catchers_y_sorted[:count_y])
        sum_y_part += sum(catchers_y_sorted[count_y:]) - y * (N - count_y)
        
        # Total distance
        total = sum_x_part + sum_y_part
        
        # Output the total distance
        print(total)
        
        # Update cumulative sums for next step
        # For x: sum_x = sum_x_part
        # For y: sum_y = sum_y_part
        
        # But we need to compute these for the next step, so we can't just store them
        # So we need to recompute them for each step
        
        # So we have to recompute the sum_x_part and sum_y_part for each step
        # Which is O(N log N) per step, which is too slow for M=3e5 and N=3e5
        
        # So we need a better way
        
        # Instead, we can precompute the sorted x and y and use prefix sums
        # Precompute prefix sums of sorted x and y
        prefix_x = [0] * (N + 1)
        prefix_y = [0] * (N + 1)
        for i in range(N):
            prefix_x[i + 1] = prefix_x[i] + catchers_x_sorted[i]
            prefix_y[i + 1] = prefix_y[i] + catchers_y_sorted[i]
        
        # Now, for each step, we can compute the sum of |x - x_i| using the prefix sums
        # Binary search for x
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if catchers_x_sorted[mid] <= x:
                left = mid + 1
            else:
                right = mid
        count_x = left
        sum_x_part = x * count_x - prefix_x[count_x]
        sum_x_part += (prefix_x[N] - prefix_x[count_x]) - x * (N - count_x)
        
        # Binary search for y
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if catchers_y_sorted[mid] <= y:
                left = mid + 1
            else:
                right = mid
        count_y = left
        sum_y_part = y * count_y - prefix_y[count_y]
        sum_y_part += (prefix_y[N] - prefix_y[count_y]) - y * (N - count_y)
        
        # Total distance
        total = sum_x_part + sum_y_part
        
        # Output the total distance
        print(total)
        
        # Update x and y for next step
        if c == 'D':
            y -= 1
        elif c == 'U':
            y += 1
        elif c == 'L':
            x -= 1
        elif c == 'R':
            x += 1

if __name__ == '__main__':
    solve()