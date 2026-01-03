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
        
        p = [0] * n
        
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
        
        # Handle the last element to ensure it is not equal to the first
        if p[-1] == p[0]:
            # Try to change the last element
            if a[-1] != p[-1]:
                p[-1] = a[-1]
            elif b[-1] != p[-1]:
                p[-1] = b[-1]
            else:
                p[-1] = c[-1]
        
        # Handle the case where the last element is still equal to the first
        if p[-1] == p[0]:
            # Try to change the first element
            if a[0] != p[-1]:
                p[0] = a[0]
            elif b[0] != p[-1]:
                p[0] = b[0]
            else:
                p[0] = c[0]
        
        print(' '.join(map(str, p)))

if __name__ == '__main__':
    solve()