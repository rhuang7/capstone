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
        possible = True
        prefix = 0
        for i in range(n):
            prefix += a[i]
            if prefix < 0:
                possible = False
                break
        if not possible:
            results.append("NO")
            continue
        suffix = 0
        for i in range(n - 1, -1, -1):
            suffix += a[i]
            if suffix < 0:
                possible = False
                break
        results.append("YES" if possible else "NO")
    print('\n'.join(results))