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
        s = a.count(1)
        b = a.count(2)
        if s == b:
            results.append(0)
            continue
        left = []
        right = []
        for i in range(2 * n):
            if a[i] == 1:
                left.append(1)
            else:
                left.append(0)
        for i in range(2 * n - 1, -1, -1):
            if a[i] == 1:
                right.append(1)
            else:
                right.append(0)
        left = left[::-1]
        left = [0] + left
        right = [0] + right
        total = 0
        for i in range(2 * n + 1):
            if left[i] == 1 and right[i] == 1:
                total += 1
        if total % 2 == 0:
            results.append(total // 2)
        else:
            results.append((total // 2) + 1)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()