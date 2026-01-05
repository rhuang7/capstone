import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
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
                # The smallest reachable value is K, and all values >= K can be formed
                # So the unreachable values are 1 to K-1
                results.append((K-1) % MOD)
            continue
        
        # For N >= 3, the minimal values are K, K+1, ..., K+N-1
        # The minimal value that can be formed is K
        # The unreachable values are those less than K and not reachable by any combination
        # Since we can form all values >= K, the unreachable values are 1 to K-1
        results.append((K-1) % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()