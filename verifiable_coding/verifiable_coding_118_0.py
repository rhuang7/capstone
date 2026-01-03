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
        n, x = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        a.sort()
        count = 0
        i = n - 1
        while i >= 0:
            if a[i] * (count + 1) >= x:
                count += 1
                i -= 1
            else:
                i -= 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()