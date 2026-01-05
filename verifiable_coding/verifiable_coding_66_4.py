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
        
        a.sort()
        b.sort()
        x = a
        y = b
        results.append(' '.join(map(str, x)))
        results.append(' '.join(map(str, y)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()