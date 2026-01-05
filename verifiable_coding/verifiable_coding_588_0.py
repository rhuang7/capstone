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
        a.append(360)
        a.sort()
        d = a[1] - a[0]
        for i in range(1, n):
            if a[i] - a[i-1] != d:
                break
        else:
            print(0)
            continue
        g = 360 // d
        for i in range(1, n):
            if a[i] % d != 0:
                break
        else:
            print(360 // d - n)
            continue
        print(360 // d - n)

if __name__ == '__main__':
    solve()