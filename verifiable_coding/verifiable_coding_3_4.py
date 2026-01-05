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
            # The maximum difference is achieved by pouring all water from the first k barrels into the last one
            # So the max is a[-1] + sum(a[:k]), the min is a[k]
            max_val = a[-1] + sum(a[:k])
            min_val = a[k]
            max_diff = max_val - min_val
        results.append(str(max_diff))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()