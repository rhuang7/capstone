import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        d = int(data[index+3])
        index += 4
        
        # Mr. Pr's position after t seconds: x = a + c * x1 + d * x2
        # Ms. Ad's position after t seconds: y = b + d * x1 + c * x2
        # We need x = y, so a + c * x1 + d * x2 = b + d * x1 + c * x2
        # Rearranging: a - b = (d - c) * x1 - (c - d) * x2
        # => a - b = (d - c) * (x1 - x2)
        # Let t = x1 + x2, then x1 - x2 = k, and t = x1 + x2
        # So x1 = (t + k)/2, x2 = (t - k)/2
        # Substitute back into equation: a - b = (d - c) * k
        # So k = (a - b) / (d - c)
        # For k to be integer, (a - b) must be divisible by (d - c)
        # Also, since x1 and x2 must be non-negative integers, t must be >= |k|
        
        if c == d:
            # If c == d, then Mr. Pr and Ms. Ad move the same distance per second
            # So their relative positions remain the same
            # So they can only meet if a == b
            if a == b:
                results.append("YES")
            else:
                results.append("NO")
            continue
        
        # Check if (a - b) is divisible by (d - c)
        if (a - b) % (d - c) != 0:
            results.append("NO")
            continue
        
        k = (a - b) // (d - c)
        
        # Check if there exists a t such that x1 and x2 are non-negative integers
        # x1 = (t + k)/2, x2 = (t - k)/2
        # So t must be >= |k| and t must have the same parity as |k|
        # Also, t must be non-negative
        
        if k >= 0:
            t_min = k
        else:
            t_min = -k
        
        # Check if there exists a t >= t_min such that t has the same parity as |k|
        # Since t can be any integer >= t_min with the same parity as |k|, it's always possible
        results.append("YES")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()