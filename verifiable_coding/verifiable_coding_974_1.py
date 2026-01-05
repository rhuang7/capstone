import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        d = int(data[index+3])
        index += 4
        
        # Mr. Pr's position after t seconds: x = a + c * t1 + d * t2
        # Ms. Ad's position after t seconds: y = b + d * t1 + c * t2
        # They meet when x = y
        # So: a + c * t1 + d * t2 = b + d * t1 + c * t2
        # Rearranging: (c - d) * t1 + (d - c) * t2 = b - a
        # => (c - d)(t1 - t2) = b - a
        # Let t = t1 - t2, then (c - d) * t = b - a
        # => t = (b - a) / (c - d)
        # But t must be an integer >= 0
        
        # Also, since both move in positive direction, t1 and t2 must be >= 0
        # So t = t1 - t2 must be >= -t2 and <= t1, but t must be integer
        
        # Check if (b - a) is divisible by (c - d)
        # Also, check if the resulting t is >= 0 and if there exists t1 and t2 such that t1 - t2 = t and t1, t2 >= 0
        
        if c == d:
            # Both move same speed, so they can't meet unless they are already at same position
            if a == b:
                print("YES")
            else:
                print("NO")
            continue
        
        if (b - a) % (c - d) != 0:
            print("NO")
            continue
        
        t = (b - a) // (c - d)
        
        # Check if t is non-negative
        if t < 0:
            print("NO")
            continue
        
        # Check if there exists t1 and t2 such that t1 - t2 = t and t1, t2 >= 0
        # t1 = t + t2
        # Since t1 >= 0, t + t2 >= 0 => t2 >= -t
        # Since t2 >= 0, t2 >= max(0, -t)
        # So there exists t2 >= 0 such that t1 = t + t2 >= 0
        # So it's always possible
        
        print("YES")

if __name__ == '__main__':
    solve()