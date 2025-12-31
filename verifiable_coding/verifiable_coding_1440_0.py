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
        # For N >= 3, the maximum cost is the second largest element
        # because (a mod b) mod c is maximized when the second largest is modded by the largest
        A.sort()
        results.append(A[-2] % A[-1])
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()