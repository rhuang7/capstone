import sys
import math
from collections import defaultdict

def compute_gcd_list(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
        if gcd == 1:
            break
    return gcd

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
            results.append(str(max(A[0], A[1])))
            continue
        max_sum = 0
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        for g in freq:
            if freq[g] >= 2:
                current_gcd = g
                for num in A:
                    if num % current_gcd == 0:
                        current_gcd = math.gcd(current_gcd, num)
                        if current_gcd == 1:
                            break
                if current_gcd > 1:
                    max_sum = max(max_sum, current_gcd + compute_gcd_list([x for x in A if x % current_gcd != 0]))
        results.append(str(max_sum))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()