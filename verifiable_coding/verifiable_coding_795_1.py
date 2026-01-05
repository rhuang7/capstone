import sys

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
        K = int(data[idx+1])
        L = int(data[idx+2])
        idx += 3
        if K < 2 or N > K * L:
            results.append("-1")
            continue
        if N == 0:
            results.append("")
            continue
        res = []
        for i in range(N):
            if i % 2 == 0:
                res.append(1)
            else:
                res.append(2)
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))