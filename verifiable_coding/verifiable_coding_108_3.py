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
        if n == 1:
            results.append("Yes")
            continue
        increasing = []
        decreasing = []
        for num in a:
            if not increasing or num > increasing[-1]:
                increasing.append(num)
            else:
                increasing.append(increasing[-1])
        for num in reversed(a):
            if not decreasing or num < decreasing[-1]:
                decreasing.append(num)
            else:
                decreasing.append(decreasing[-1])
        increasing = increasing[:-1]
        decreasing = decreasing[:-1]
        if len(increasing) + len(decreasing) == n:
            results.append("Yes")
        else:
            results.append("No")
    print("\n".join(results))

if __name__ == '__main__':
    solve()