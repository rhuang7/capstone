import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        n = len(s)
        d = 0
        pos = 0
        
        while pos < n:
            if s[pos] == 'R':
                d = max(d, pos + 1)
                pos += 1
            else:
                d = max(d, pos + 1)
                pos = 0
        
        # Check if the frog can jump directly from 0 to n+1
        if d < n + 1:
            d = n + 1
        
        results.append(str(d))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()