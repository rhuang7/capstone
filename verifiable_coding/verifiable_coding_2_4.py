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
        # Choose p[0] as a[0]
        p[0] = a[0]
        # Fill the rest
        for i in range(1, n):
            # Choose a value from a[i], b[i], c[i] that is not equal to p[i-1]
            for val in [a[i], b[i], c[i]]:
                if val != p[i-1]:
                    p[i] = val
                    break
        # Check the last and first element
        if p[-1] == p[0]:
            # If they are equal, try to change the last element
            for val in [a[-1], b[-1], c[-1]]:
                if val != p[-2] and val != p[0]:
                    p[-1] = val
                    break
        print(' '.join(map(str, p)))

if __name__ == '__main__':
    solve()