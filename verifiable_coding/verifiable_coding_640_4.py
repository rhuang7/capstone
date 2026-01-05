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
        
        # Find the least common multiple of X and Y
        def lcm(a, b):
            from math import gcd
            return a * b // gcd(a, b)
        
        l = lcm(X, Y)
        power = (l // X - 1) + (l // Y - 1)
        results.append(str(power))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()