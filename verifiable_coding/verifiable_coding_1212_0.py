import sys
from collections import Counter

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for s in cases:
        cnt = Counter(s)
        freq = list(cnt.values())
        n = len(s)
        total = sum(freq)
        m = len(freq)
        freq.sort(reverse=True)
        res = 0
        for i in range(m):
            if i == 0:
                target = n // m
            else:
                target = n // (m - i)
            if freq[i] > target:
                res += freq[i] - target
        print(res)

if __name__ == '__main__':
    solve()