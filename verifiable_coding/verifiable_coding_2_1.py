import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        c = list(map(int, data[idx:idx+n]))
        idx += n
        p = [0]*n
        # Choose p[0] from a[0], b[0], c[0]
        p[0] = a[0]
        for i in range(1, n):
            # Choose p[i] from a[i], b[i], c[i] that is not equal to p[i-1]
            for val in [a[i], b[i], c[i]]:
                if val != p[i-1]:
                    p[i] = val
                    break
        # Check if p[n-1] != p[0], if not, change p[0]
        if p[-1] == p[0]:
            for val in [a[0], b[0], c[0]]:
                if val != p[-1] and val != p[1]:
                    p[0] = val
                    break
        print(' '.join(map(str, p)))

if __name__ == '__main__':
    solve()