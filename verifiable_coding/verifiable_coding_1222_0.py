import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    strings = input[1:T+1]

    for s in strings:
        n = len(s)
        count = 0
        freq = Counter()
        for i in range(n):
            freq[tuple(sorted(s[i:]))] += 1
        for v in freq.values():
            count += v * (v - 1) // 2
        print(count)

if __name__ == '__main__':
    solve()