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
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        possible = True
        for i in range(1, n + 1):
            if prefix[i] != prefix[i - 1]:
                possible = False
                break
        results.append("YES" if possible else "NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()