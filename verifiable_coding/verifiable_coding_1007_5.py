import sys
import math
from math import gcd
from functools import reduce

def compute_gcd_list(arr):
    return reduce(gcd, arr)

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
        max_len = -1
        for i in range(N):
            current_gcd = 0
            for j in range(i, N):
                current_gcd = math.gcd(current_gcd, A[j])
                if current_gcd == 1:
                    max_len = max(max_len, j - i + 1)
        if max_len == -1:
            results.append("-1")
        else:
            results.append(str(max_len))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()