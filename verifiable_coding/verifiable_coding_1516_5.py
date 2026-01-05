import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        if N == 2:
            if K == 1:
                results.append(0)
            else:
                # Unreachable values are 1, 2, ..., K-1
                res = (K - 1) % MOD
                results.append(res)
        else:
            # For N >= 3, the minimal reachable values are 1, 2, ..., N-1
            # So all values >= 1 are reachable
            results.append(0)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()