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
        # The optimal way is to have one class of size 1 and the other of size 2n-1
        # Or vice versa, but the minimal difference is always between a[0] and a[2n-1]
        # Because the median of the class of size 1 is the element itself
        # The median of the class of size 2n-1 is the nth element (0-based)
        # So the minimal difference is |a[0] - a[n]|
        results.append(str(abs(a[0] - a[n])))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()