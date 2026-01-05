import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        X = int(data[idx])
        Y = int(data[idx+1])
        idx += 2
        
        def min_jumps(n):
            if n == 0:
                return 0
            # Find the minimum number of jumps to reach n using jumps of 2^k - 1
            # The optimal way is to use the largest possible jumps first
            jumps = 0
            while n > 0:
                # Find the largest 2^k - 1 <= n
                k = math.floor(math.log2(n + 1))
                jump = (1 << k) - 1
                n -= jump
                jumps += 1
            return jumps
        
        jumps_x = min_jumps(X)
        jumps_y = min_jumps(Y)
        if jumps_x < jumps_y:
            results.append("1 {}".format(jumps_y - jumps_x))
        elif jumps_y < jumps_x:
            results.append("2 {}".format(jumps_x - jumps_y))
        else:
            results.append("0 0")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()