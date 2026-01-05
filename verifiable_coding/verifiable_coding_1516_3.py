import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        if N == 2:
            if K == 1:
                results.append(0)
            else:
                # The smallest unreachable value is K-1
                # All values >= K can be formed by adding K and 1
                results.append(K-1)
        else:
            # For N >= 3, the smallest unreachable value is K-1
            # All values >= K can be formed by adding K and some value from 1 to N-1
            results.append(K-1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()