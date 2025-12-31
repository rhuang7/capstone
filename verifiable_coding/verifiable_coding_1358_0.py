import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        w = input[idx]
        K = int(input[idx+1])
        idx += 2
        count = Counter(w)
        freq = list(count.values())
        freq.sort()
        n = len(freq)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if abs(freq[i] - freq[j]) > K:
                    res += 1
        print(res)

if __name__ == '__main__':
    solve()