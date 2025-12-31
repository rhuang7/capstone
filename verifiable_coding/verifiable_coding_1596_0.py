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
            # Find the minimum number of jumps using powers of 2
            # The optimal strategy is to use the largest possible jump each time
            # So we find the largest 2^k - 1 <= n
            # The number of jumps is the number of bits set in the binary representation of n
            # Because each jump can be a power of 2 minus 1, and we need to cover n with such jumps
            # For example, 5 = 3 + 2, which is 2^2 - 1 + 2^1 - 1
            # So the number of jumps is the number of 1s in binary representation of n
            return bin(n).count('1')
        
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