import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        X = int(data[idx])
        Y = int(data[idx + 1])
        idx += 2
        
        if X == Y:
            results.append('0')
            continue
        
        # Find the minimum power such that X * (k) == Y * (k)
        # Which is equivalent to finding the least common multiple (LCM) of X and Y
        # Power required is LCM(X, Y) / X + LCM(X, Y) / Y - X - Y
        # But since LCM(X, Y) = (X * Y) // GCD(X, Y)
        # Power = (Y // GCD(X, Y)) + (X // GCD(X, Y)) - X - Y
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        g = gcd(X, Y)
        lcm = (X * Y) // g
        power = (lcm // X) + (lcm // Y) - X - Y
        results.append(str(power))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()