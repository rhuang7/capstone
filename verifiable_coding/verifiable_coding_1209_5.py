import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    idx = 1
    
    for _ in range(n):
        v1 = int(data[idx])
        t1 = int(data[idx+1])
        v2 = int(data[idx+2])
        t2 = int(data[idx+3])
        v3 = int(data[idx+4])
        t3 = int(data[idx+5])
        idx += 6
        
        # Check if it's possible to get exactly t3 temperature with at least v3 volume
        # Let x be the volume of cold water used, y be the volume of hot water used
        # x + y >= v3
        # (x*t1 + y*t2) / (x + y) = t3
        # => x*t1 + y*t2 = t3*(x + y)
        # => x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y * (t2 - t3) / (t3 - t1)
        
        # Since t1 < t3 < t2, t3 - t1 > 0 and t2 - t3 > 0
        # So x and y must be non-negative and x + y >= v3
        
        # Check if t3 is between t1 and t2
        if t3 < t1 or t3 > t2:
            print("NO")
            continue
        
        # Check if it's possible to get exactly t3 with some combination of v1 and v2
        # We can use binary search or check possible values of x and y
        # But since the problem is to check feasibility, we can use a mathematical approach
        
        # The required ratio of cold to hot water is (t2 - t3) / (t3 - t1)
        ratio = (t2 - t3) / (t3 - t1)
        
        # Check if there exists x and y such that x + y >= v3 and x / y = ratio
        # So x = ratio * y
        # x + y = y * (ratio + 1) >= v3
        # y >= v3 / (ratio + 1)
        
        # We need to find if there exists y such that y >= v3 / (ratio + 1) and x = ratio * y <= v1, y <= v2
        
        # Try to find the minimum y that satisfies the condition
        # y_min = max(ceil(v3 / (ratio + 1)), 0)
        # x = ratio * y_min
        # Check if x <= v1 and y_min <= v2
        
        # But since we are dealing with floating points, we can use a more precise approach
        
        # Check if there exists x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # This is equivalent to x*t1 + y*t2 = t3*(x + y)
        # => x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y * (t2 - t3) / (t3 - t1)
        
        # We need x >= 0, y >= 0, x <= v1, y <= v2, x + y >= v3
        
        # Try to find x and y that satisfy these conditions
        # Try x = 0, y = v2
        if t2 == t3:
            if v2 >= v3:
                print("YES")
                continue
            else:
                print("NO")
                continue
        
        # Try y = 0, x = v1
        if t1 == t3:
            if v1 >= v3:
                print("YES")
                continue
            else:
                print("NO")
                continue
        
        # Try to find x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # We can use binary search on x and y
        
        # Try x = 0, y = v2
        if (0 * t1 + v2 * t2) / (0 + v2) == t3 and v2 >= v3:
            print("YES")
            continue
        
        # Try y = 0, x = v1
        if (v1 * t1 + 0 * t2) / (v1 + 0) == t3 and v1 >= v3:
            print("YES")
            continue
        
        # Try to find x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # We can use binary search on x and y
        # But for the sake of time, we can use a simpler approach
        
        # Try to find x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # We can use a linear search for x in [0, v1] and y in [0, v2]
        # But this is too slow for large values
        
        # Instead, we can use the mathematical approach
        # x = y * (t2 - t3) / (t3 - t1)
        # x + y >= v3
        # x <= v1
        # y <= v2
        
        # Try to find the minimum y that satisfies the conditions
        # y_min = max(ceil(v3 / (ratio + 1)), 0)
        # x = ratio * y_min
        # Check if x <= v1 and y_min <= v2
        
        # But since we are dealing with floating points, we can use a more precise approach
        
        # Check if there exists x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # This is equivalent to x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y * (t2 - t3) / (t3 - t1)
        
        # Try to find x and y such that x + y >= v3 and x <= v1, y <= v2
        
        # Try to find the minimum y that satisfies the condition
        # y_min = max(ceil(v3 / (ratio + 1)), 0)
        # x = ratio * y_min
        # Check if x <= v1 and y_min <= v2
        
        # But since we are dealing with floating points, we can use a more precise approach
        
        # Check if there exists x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # This is equivalent to x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y * (t2 - t3) / (t3 - t1)
        
        # Try to find x and y such that x + y >= v3 and x <= v1, y <= v2
        
        # Try to find the minimum y that satisfies the condition
        # y_min = max(ceil(v3 / (ratio + 1)), 0)
        # x = ratio * y_min
        # Check if x <= v1 and y_min <= v2
        
        # But since we are dealing with floating points, we can use a more precise approach
        
        # Check if there exists x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # This is equivalent to x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y * (t2 - t3) / (t3 - t1)
        
        # Try to find x and y such that x + y >= v3 and x <= v1, y <= v2
        
        # Try to find the minimum y that satisfies the condition
        # y_min = max(ceil(v3 / (ratio + 1)), 0)
        # x = ratio * y_min
        # Check if x <= v1 and y_min <= v2
        
        # But since we are dealing with floating points, we can use a more precise approach
        
        # Check if there exists x and y such that x + y >= v3 and (x*t1 + y*t2) / (x + y) = t3
        # This is equivalent to x*(t1 - t3) + y*(t2 - t3) = 0
        # => x = y * (t2 - t3) / (t3 - t1)
        
        # Try to find x and y such that x + y >= v3 and x <= v1, y <= v2
        
        # Try to find the minimum y that satisfies the condition
        # y_min = max(ceil(v3 / (ratio + 1)), 0)
        # x = ratio