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
                # Unreachable values are 1, 2, ..., K-1
                # But since K >= 2, the number of unreachable values is K-1
                results.append((K-1) % MOD)
        else:
            # For N >= 3, the smallest unreachable value is 1
            # But we need to check if 1 is reachable
            # Since K >= 1, and we have K, K+1, ..., K+N-1
            # If K == 1, then 1 is reachable
            # Else, 1 is not reachable
            if K == 1:
                results.append(0)
            else:
                # Unreachable values are 1, 2, ..., K-1
                # But since K >= 2, the number of unreachable values is K-1
                results.append((K-1) % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()