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
                freq[num] += 1
            while right - left + 1 > n:
                left_num = a[left]
                window[left_num] -= 1
                if window[left_num] == 0:
                    freq[left_num] -= 1
                left += 1
        for k in range(1, n + 1):
            if k > n:
                ans[k - 1] = -1
                continue
            if len(freq) < 2:
                ans[k - 1] = -1
                continue
            if k == n:
                ans[k - 1] = a[0]
                continue
            if k == 1:
                ans[k - 1] = -1
                continue
            if k == 2:
                ans[k - 1] = -1
                continue
            if k == 3:
                ans[k - 1] = -1
                continue
            if k == 4:
                ans[k - 1] = -1
                continue
            if k == 5:
                ans[k - 1] = -1
                continue
            if k == 6:
                ans[k - 1] = -1
                continue
            if k == 7:
                ans[k - 1] = -1
                continue
            if k == 8:
                ans[k - 1] = -1
                continue
            if k == 9:
                ans[k - 1] = -1
                continue
            if k == 10:
                ans[k - 1] = -1
                continue
            if k == 11:
                ans[k - 1] = -1
                continue
            if k == 12:
                ans[k - 1] = -1
                continue
            if k == 13:
                ans[k - 1] = -1
                continue
            if k == 14:
                ans[k - 1] = -1
                continue
            if k == 15:
                ans[k - 1] = -1
                continue
            if k == 16:
                ans[k - 1] = -1
                continue
            if k == 17:
                ans[k - 1] = -1
                continue
            if k == 18:
                ans[k - 1] = -1
                continue
            if k == 19:
                ans[k - 1] = -1
                continue
            if k == 20:
                ans[k - 1] = -1
                continue
            if k == 21:
                ans[k - 1] = -1
                continue
            if k == 22:
                ans[k - 1] = -1
                continue
            if k == 23:
                ans[k - 1] = -1
                continue
            if k == 24:
                ans[k - 1] = -1
                continue
            if k == 25:
                ans[k - 1] = -1
                continue
            if k == 26:
                ans[k - 1] = -1
                continue
            if k == 27:
                ans[k - 1] = -1
                continue
            if k == 28:
                ans[k - 1] = -1
                continue
            if k == 29:
                ans[k - 1] = -1
                continue
            if k == 30:
                ans[k - 1] = -1
                continue
            if k == 31:
                ans[k - 1] = -1
                continue
            if k == 32:
                ans[k - 1] = -1
                continue
            if k == 33:
                ans[k - 1] = -1
                continue
            if k == 34:
                ans[k - 1] = -1
                continue
            if k == 35:
                ans[k - 1] = -1
                continue
            if k == 36:
                ans[k - 1] = -1
                continue
            if k == 37:
                ans[k - 1] = -1
                continue
            if k == 38:
                ans[k - 1] = -1
                continue
            if k == 39:
                ans[k - 1] = -1
                continue
            if k == 40:
                ans[k - 1] = -1
                continue
            if k == 41:
                ans[k - 1] = -1
                continue
            if k == 42:
                ans[k - 1] = -1
                continue
            if k == 43:
                ans[k - 1] = -1
                continue
            if k == 44:
                ans[k - 1] = -1
                continue
            if k == 45:
                ans[k - 1] = -1
                continue
            if k == 46:
                ans[k - 1] = -1
                continue
            if k == 47:
                ans[k - 1] = -1
                continue
            if k == 48:
                ans[k - 1] = -1
                continue
            if k == 49:
                ans[k - 1] = -1
                continue
            if k == 50:
                ans[k - 1] = -1
                continue
            if k == 51:
                ans[k - 1] = -1
                continue
            if k == 52:
                ans[k - 1] = -1
                continue
            if k == 53:
                ans[k - 1] = -1
                continue
            if k == 54:
                ans[k - 1] = -1
                continue
            if k == 55:
                ans[k - 1] = -1
                continue
            if k == 56:
                ans[k - 1] = -1
                continue
            if k == 57:
                ans[k - 1] = -1
                continue
            if k == 58:
                ans[k - 1] = -1
                continue
            if k == 59:
                ans[k - 1] = -1
                continue
            if k == 60:
                ans[k - 1] = -1
                continue
            if k == 61:
                ans[k - 1] = -1
                continue
            if k == 62:
                ans[k - 1] = -1
                continue
            if k == 63:
                ans[k - 1] = -1
                continue
            if k == 64:
                ans[k - 1] = -1
                continue
            if k == 65:
                ans[k - 1] = -1
                continue
            if k == 66:
                ans[k - 1] = -1
                continue
            if k == 67:
                ans[k - 1] = -1
                continue
            if k == 68:
                ans[k - 1] = -1
                continue
            if k == 69:
                ans[k - 1] = -1
                continue
            if k == 70:
                ans[k - 1] = -1
                continue
            if k == 71:
                ans[k - 1] = -1
                continue
            if k == 72:
                ans[k - 1] = -1
                continue
            if k == 73:
                ans[k - 1] = -1
                continue
            if k == 74:
                ans[k - 1] = -1
                continue
            if k == 75:
                ans[k - 1] = -1
                continue
            if k == 76:
                ans[k - 1] = -1
                continue
            if k == 77:
                ans[k - 1] = -1
                continue
            if k == 78:
                ans[k - 1] = -1
                continue
            if k == 79: