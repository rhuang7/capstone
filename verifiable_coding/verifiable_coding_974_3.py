import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        d = int(data[idx+3])
        idx += 4
        
        # Mr. Pr's position after t seconds: x = a + c * t1 + d * t2
        # Ms. Ad's position after t seconds: y = b + d * t1 + c * t2
        # They meet when x = y
        # So: a + c * t1 + d * t2 = b + d * t1 + c * t2
        # Rearranging: (c - d) * t1 + (d - c) * t2 = b - a
        # => (c - d)(t1 - t2) = b - a
        # Let t = t1 + t2, then t1 - t2 = k, and t1 = (t + k)/2, t2 = (t - k)/2
        # Substitute into equation: (c - d) * k = b - a
        # So k = (b - a) / (c - d)
        # For k to be integer, (b - a) must be divisible by (c - d)
        # Also, since t1 and t2 are non-negative, we must have t1 >= 0 and t2 >= 0
        # So (t + k)/2 >= 0 and (t - k)/2 >= 0 => t >= |k|
        # But t is the total time, which is non-negative, so t >= |k|
        # So for some integer t >= |k|, the equation holds
        
        # Check if (b - a) is divisible by (c - d)
        if c == d:
            # If c == d, then the relative speed is zero
            # So they can only meet if a == b
            if a == b:
                print("YES")
            else:
                print("NO")
            continue
        
        if (b - a) % (c - d) != 0:
            print("NO")
            continue
        
        k = (b - a) // (c - d)
        # Check if there exists t >= |k| such that t1 and t2 are non-negative
        # t1 = (t + k)/2, t2 = (t - k)/2
        # For t1 and t2 to be non-negative, t >= |k|
        # So we can choose t = |k|, and check if t1 and t2 are non-negative
        t = abs(k)
        t1 = (t + k) // 2
        t2 = (t - k) // 2
        if t1 >= 0 and t2 >= 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()