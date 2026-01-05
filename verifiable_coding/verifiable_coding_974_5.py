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
        # Simplify: a - b = (d - c) * (x1 - x2)
        # Let t = x1 + x2, then x1 - x2 = k, and t = x1 + x2
        # So a - b = (d - c) * k
        # We need to find integers k and t such that k + t is even and t >= 0
        
        diff = a - b
        if diff == 0:
            results.append("YES")
            continue
        
        if (d - c) == 0:
            results.append("NO")
            continue
        
        if (diff % (d - c)) != 0:
            results.append("NO")
            continue
        
        # Check if there exists a non-negative integer t such that t = (x1 + x2) and k = x1 - x2
        # Since k = diff / (d - c), and t = x1 + x2, then x1 = (t + k) / 2, x2 = (t - k) / 2
        # Both x1 and x2 must be non-negative integers
        # So t + k must be even and t - k must be even
        # Which implies t and k have the same parity
        
        k = diff // (d - c)
        if (k % 2 == 0) and (k >= 0):
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()