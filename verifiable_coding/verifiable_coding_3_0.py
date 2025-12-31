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
        max_val = a[-1]
        min_val = a[0]
        if k == 0:
            results.append(str(max_val - min_val))
            continue
        # We can pour from the first k barrels to the last one
        # So the max possible difference is (sum of first k barrels) + a[-1] - a[0]
        # But since we can pour any amount, the max is when we pour all from first k barrels to the last one
        # So the max value is a[-1] + sum(a[:k])
        # The min value is a[0]
        max_diff = a[-1] + sum(a[:k]) - a[0]
        results.append(str(max_diff))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()