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
        # because the maximum possible value of (x mod y) is y-1
        # So we choose the maximum element as y and the second maximum as x
        # The maximum cost is (second_max - 1)
        max_val = max(A)
        second_max = -1
        for num in A:
            if num != max_val:
                second_max = max(second_max, num)
        results.append(second_max - 1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()