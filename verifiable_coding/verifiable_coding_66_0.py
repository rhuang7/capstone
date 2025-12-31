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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        a.sort()
        b.sort()
        
        # We can pair the smallest a with the largest b, and so on
        # to ensure all sums are unique
        x = a
        y = [b[-i-1] for i in range(n)]
        
        results.append(' '.join(map(str, x)))
        results.append(' '.join(map(str, y)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()