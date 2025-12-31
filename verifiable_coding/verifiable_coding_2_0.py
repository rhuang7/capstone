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
        # Iterate through the rest
        for i in range(1, n):
            # Choose a value from a[i], b[i], c[i] that is not equal to p[i-1]
            if a[i] != p[i-1]:
                p[i] = a[i]
            elif b[i] != p[i-1]:
                p[i] = b[i]
            else:
                p[i] = c[i]
        # Check if the last element is different from the first
        if p[-1] == p[0]:
            # If not, change the first element to something else
            # Try to find a value for p[0] that is not equal to p[-1]
            for val in [a[0], b[0], c[0]]:
                if val != p[-1]:
                    p[0] = val
                    break
        print(' '.join(map(str, p)))

if __name__ == '__main__':
    solve()