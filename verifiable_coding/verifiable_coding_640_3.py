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
        # The power is the minimum number of times we need to multiply X or Y to reach a common value
        # So we need to find the least common multiple (LCM) of X and Y, then compute the power required
        # Power is (LCM / X) + (LCM / Y) - 1  # because we don't count the initial value
        # But since we can only multiply, we need to find the minimum number of multiplications
        # So the correct approach is to find the minimum number of multiplications needed to make X and Y equal
        
        # Find the LCM of X and Y
        def lcm(a, b):
            from math import gcd
            return a * b // gcd(a, b)
        
        l = lcm(X, Y)
        power = (l // X) + (l // Y) - 1
        results.append(str(power))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()