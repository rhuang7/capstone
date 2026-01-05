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
        cnt = Counter(w)
        freq = list(cnt.values())
        freq.sort()
        res = 0
        for i in range(len(freq)):
            for j in range(i+1, len(freq)):
                if abs(freq[i] - freq[j]) > K:
                    res += abs(freq[i] - freq[j]) - K
        print(res)

if __name__ == '__main__':
    solve()