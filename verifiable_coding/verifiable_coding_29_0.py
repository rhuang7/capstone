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
            if right >= n - 1:
                if len(window) == 1:
                    ans[n - 1] = a[right]
                else:
                    ans[n - 1] = -1
                left = right - n + 1
                while left <= right:
                    if window[a[left]] == 1:
                        del window[a[left]]
                    else:
                        window[a[left]] -= 1
                    left += 1
        for k in range(1, n):
            if k == 1:
                ans[0] = -1
                continue
            window = collections.defaultdict(int)
            left = 0
            for right in range(n):
                window[a[right]] += 1
                if right >= k - 1:
                    if len(window) == 1:
                        ans[k - 1] = a[right]
                    else:
                        ans[k - 1] = -1
                    while left <= right:
                        if window[a[left]] == 1:
                            del window[a[left]]
                        else:
                            window[a[left]] -= 1
                        left += 1
        results.append(' '.join(map(str, ans)))
    print('\n'.join(results))