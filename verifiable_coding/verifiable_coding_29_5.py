import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        ans = [-1] * n
        freq = collections.defaultdict(int)
        window = collections.defaultdict(int)
        left = 0
        for right in range(n):
            x = a[right]
            window[x] += 1
            if window[x] == 1:
                freq[x] = 1
            while right - left + 1 > n - 1:
                y = a[left]
                window[y] -= 1
                if window[y] == 0:
                    del window[y]
                left += 1
            if len(window) == 1:
                ans[n - 1 - (right - left + 1)] = window[window.keys()[0]]
        results.append(' '.join(map(str, ans)))
    print('\n'.join(results))