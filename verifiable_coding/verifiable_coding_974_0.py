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
        # So t = (b - a) / (c - d)
        # But t must be an integer >= 0
        
        if c == d:
            # If c == d, then the relative speed is zero, so they can only meet if they are already at the same position
            if a == b:
                print("YES")
            else:
                print("NO")
            continue
        
        # Check if (b - a) is divisible by (c - d)
        # Also, t must be >= 0
        if (b - a) % (c - d) == 0:
            t = (b - a) // (c - d)
            if t >= 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

if __name__ == '__main__':
    solve()