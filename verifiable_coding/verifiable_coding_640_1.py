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
        
        # Find the minimum power required to make X and Y equal
        # The power is the minimum value of (k * X) and (k * Y) such that k * X = k * Y
        # So, find the least common multiple (LCM) of X and Y
        # Power is LCM / X if X < Y, else LCM / Y
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        g = gcd(X, Y)
        lcm = (X * Y) // g
        
        if X < Y:
            power = lcm // X
        else:
            power = lcm // Y
        
        results.append(str(power))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()