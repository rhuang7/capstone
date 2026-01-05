import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for S in cases:
        cnt = Counter(S)
        freq = list(cnt.values())
        n = len(S)
        freq.sort()
        m = len(freq)
        total = 0
        for i in range(m):
            if i < m - 1:
                total += (freq[i] - freq[i + 1]) * (m - i - 1)
            else:
                total += (freq[i] - (n // m)) * (m - i - 1)
        print(total)

if __name__ == '__main__':
    solve()