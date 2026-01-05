import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        a.sort()
        # The optimal way is to have classes of sizes 1 and 2n-1, or 2n-1 and 1
        # The medians will be a[0] and a[2n-1], or a[2n-1] and a[0]
        # The minimal difference is the absolute difference between a[0] and a[2n-1]
        # But wait, there's a better way: the minimal difference is always a[2n-1] - a[0]
        # Because the optimal way is to have one class of size 1 (median is a[0]) and the other of size 2n-1 (median is a[2n-1])
        # Or vice versa, but the difference is the same
        results.append(str(a[-1] - a[0]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()