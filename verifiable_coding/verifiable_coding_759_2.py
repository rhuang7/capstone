import sys
import math
from collections import defaultdict

def largest_prime_factor(n):
    if n == 1:
        return 1
    largest = -1
    while n % 2 == 0:
        largest = 2
        n //= 2
    i = 3
    while i <= int(math.sqrt(n)) + 1:
        while n % i == 0:
            largest = i
            n //= i
        i += 2
    if n > 1:
        largest = n
    return largest

def solve():
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
        lpf_counts = defaultdict(int)
        for num in A:
            lpf = largest_prime_factor(num)
            lpf_counts[lpf] += 1
        max_count = -1
        result = 1
        for key in lpf_counts:
            if lpf_counts[key] > max_count or (lpf_counts[key] == max_count and key > result):
                max_count = lpf_counts[key]
                result = key
        results.append(str(result))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()