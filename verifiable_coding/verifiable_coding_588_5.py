import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx+n]))
        idx += n
        a.append(0)
        a.sort()
        d = a[1] - a[0]
        for i in range(1, n):
            if a[i] - a[i-1] != d:
                d = -1
                break
        if d == -1:
            print(0)
            continue
        g = 360 // d
        if 360 % d != 0:
            g = 360 // d
        cnt = 0
        for angle in a:
            if angle % g != 0:
                cnt += 1
        print(360 // g - cnt)

if __name__ == '__main__':
    solve()