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
        # a + c * t1 + d * t2 = b + d * t1 + c * t2
        # Rearranging: (c - d) * t1 + (d - c) * t2 = b - a
        # (c - d)(t1 - t2) = b - a
        # Let t = t1 - t2, then (c - d) * t = b - a
        # So t = (b - a) / (c - d)
        # For t to be integer, (b - a) must be divisible by (c - d) and t must be non-negative
        # Also, since both move in positive direction, t must be >= 0
        
        if c == d:
            # If c == d, then both move same speed, so they can only meet if a == b
            if a == b:
                print("YES")
            else:
                print("NO")
            continue
        
        if (b - a) % (c - d) != 0:
            print("NO")
            continue
        
        t = (b - a) // (c - d)
        if t >= 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()