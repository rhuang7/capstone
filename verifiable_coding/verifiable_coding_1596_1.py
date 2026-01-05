import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index + 1])
        index += 2
        
        def min_jumps(n):
            if n == 0:
                return 0
            jumps = 0
            remaining = n
            while remaining > 0:
                # Use the largest possible step
                step = 1 << (remaining.bit_length() - 1)
                remaining -= step
                jumps += 1
            return jumps
        
        j1 = min_jumps(X)
        j2 = min_jumps(Y)
        
        if j1 < j2:
            results.append("1 {}".format(j2 - j1))
        elif j1 > j2:
            results.append("2 {}".format(j1 - j2))
        else:
            results.append("0 0")
    
    print('\n'.join(results))