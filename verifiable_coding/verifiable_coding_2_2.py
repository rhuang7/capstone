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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+n]))
        idx += n
        c = list(map(int, data[idx:idx+n]))
        idx += n
        
        p = [0] * n
        for i in range(n):
            if i == 0:
                # Choose the first element
                p[i] = a[i]
            else:
                # Choose a value different from previous
                if p[i-1] == a[i]:
                    p[i] = b[i]
                elif p[i-1] == b[i]:
                    p[i] = a[i]
                else:
                    p[i] = c[i]
        
        # Check if the last and first elements are different
        if p[-1] == p[0]:
            # If not, try to change the first element
            for i in range(n):
                if p[i] == p[0]:
                    # Try to change p[i] to a different value
                    if p[i] == a[i]:
                        p[i] = b[i]
                    elif p[i] == b[i]:
                        p[i] = a[i]
                    else:
                        p[i] = c[i]
                    # Check if this fixes the issue
                    if p[-1] != p[0]:
                        break
        
        results.append(' '.join(map(str, p)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()