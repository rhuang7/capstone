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
        # Choose p[0]
        p[0] = a[0]
        # Choose p[1] to p[n-1]
        for i in range(1, n):
            # Choose a value from a[i], b[i], c[i] that is not equal to p[i-1]
            if a[i] != p[i-1]:
                p[i] = a[i]
            elif b[i] != p[i-1]:
                p[i] = b[i]
            else:
                p[i] = c[i]
        # Check if p[n-1] != p[0]
        if p[-1] == p[0]:
            # If not, try to change p[0] to something else
            for val in [b[0], c[0]]:
                if val != p[-1]:
                    p[0] = val
                    break
        print(' '.join(map(str, p)))

if __name__ == '__main__':
    solve()