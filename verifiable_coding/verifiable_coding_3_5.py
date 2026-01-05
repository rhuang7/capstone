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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort()
        max_diff = 0
        if k == 0:
            max_diff = a[-1] - a[0]
        else:
            # We can pour water from the first k barrels to the last (n - k) barrels
            # The maximum difference is the sum of the first k barrels (all poured into the last one)
            # The minimum is 0 (since we can pour all water from the first k barrels)
            max_diff = sum(a[:k])
        results.append(str(max_diff))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()