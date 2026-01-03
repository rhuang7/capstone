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
            num = a[right]
            window[num] += 1
            if window[num] == 1:
                freq[num] = 1
            while right - left + 1 > n - 1:
                left_num = a[left]
                window[left_num] -= 1
                if window[left_num] == 0:
                    del window[left_num]
                left += 1
            if len(window) == 1:
                ans[n - 1 - (right - left + 1)] = list(window.keys())[0]
        results.append(' '.join(map(str, ans)))
    print('\n'.join(results))