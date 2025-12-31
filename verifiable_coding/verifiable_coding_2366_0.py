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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        bad = 0
        min_price = float('inf')
        for i in range(n-1, -1, -1):
            if a[i] < min_price:
                bad += 1
            min_price = min(min_price, a[i])
        results.append(str(bad))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()