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
            window[a[right]] += 1
            freq[a[right]] += 1
            if right - left + 1 > n:
                left += 1
            if right - left + 1 == n:
                for key in list(window.keys()):
                    if window[key] == 1:
                        del window[key]
                for key in list(freq.keys()):
                    if freq[key] == 1:
                        del freq[key]
                if len(window) == 1:
                    ans[n - 1] = list(window.keys())[0]
        for k in range(1, n):
            if k == n:
                ans[k - 1] = list(window.keys())[0] if len(window) == 1 else -1
            else:
                freq = collections.defaultdict(int)
                window = collections.defaultdict(int)
                left = 0
                for right in range(n):
                    window[a[right]] += 1
                    freq[a[right]] += 1
                    if right - left + 1 > k:
                        left += 1
                    if right - left + 1 == k:
                        for key in list(window.keys()):
                            if window[key] == 1:
                                del window[key]
                        for key in list(freq.keys()):
                            if freq[key] == 1:
                                del freq[key]
                        if len(window) == 1:
                            ans[k - 1] = list(window.keys())[0]
        results.append(' '.join(map(str, ans)))
    print('\n'.join(results))