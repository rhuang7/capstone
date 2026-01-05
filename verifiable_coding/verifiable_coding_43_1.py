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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
        max_time = 0
        for i in range(n):
            max_time = max(max_time, a[i], b[i])
        results.append(str(max_time))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()