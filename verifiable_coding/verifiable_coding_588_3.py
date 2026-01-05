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
        g = d
        for i in range(1, n):
            g = math.gcd(g, a[i+1] - a[i])
        res = 360 // g - n
        print(res)

if __name__ == '__main__':
    solve()