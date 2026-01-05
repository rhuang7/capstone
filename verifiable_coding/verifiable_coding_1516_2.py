import sys
import math

MOD = 10**9 + 7

def solve():
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
                # The smallest reachable value is K, and we can generate all values >= K
                # So no unreachable values
                results.append(0)
        else:
            # For N >= 3, the minimal unreachable values are those less than K
            # But since we can generate any value >= K, the number of unreachable values is K-1
            results.append((K-1) % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()