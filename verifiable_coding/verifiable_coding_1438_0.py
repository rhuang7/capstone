import sys
import math
from collections import defaultdict

def compute_s(x):
    s = 0
    i = 2
    while i * i <= x:
        if x % i == 0:
            s += i
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        s += x
    return s

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        s_map = defaultdict(int)
        for num in a:
            s = compute_s(num)
            s_map[s] += 1
        count = 0
        for s_val in s_map:
            freq = s_map[s_val]
            for s2_val in s_map:
                if s2_val % s_val == 0:
                    count += freq * s_map[s2_val]
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()