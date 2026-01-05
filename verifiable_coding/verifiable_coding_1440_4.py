import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        if N == 2:
            results.append(max(A[0] % A[1], A[1] % A[0]))
            continue
        
        # For N >= 3, the maximum cost is the maximum element minus 1
        # because the maximum value mod any other value is at most that value - 1
        max_val = max(A)
        results.append(max_val - 1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()