import sys

def solve():
    from collections import Counter

    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1

    target = Counter("codechef")
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        counts = Counter()
        for _ in range(N):
            s = input[idx]
            idx += 1
            counts += Counter(s)
        res = 0
        for c in target:
            res += counts[c] // target[c]
        print(res)

if __name__ == '__main__':
    solve()