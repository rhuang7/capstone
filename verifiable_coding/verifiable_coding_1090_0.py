import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n, d = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + a[i]
        min_len = -1
        for i in range(n+1):
            target = d - prefix[i]
            j = bisect.bisect_left(prefix, target, i+1, n+1)
            if j != n+1:
                min_len = min(min_len, j - i) if min_len != -1 else j - i
        results.append(str(min_len) if min_len != -1 else "-1")
    print('\n'.join(results))