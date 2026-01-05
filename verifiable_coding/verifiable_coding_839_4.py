import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        k = int(data[idx])
        idx += 1
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = sum(a)
        if total >= k:
            results.append('1')
        else:
            results.append('0')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()