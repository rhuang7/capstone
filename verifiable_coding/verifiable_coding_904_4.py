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
        N = int(data[idx])
        X = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = 0
        for i in range(N):
            if (i+1) % 2 == 1:
                total += a[i]
            if total >= X:
                results.append("YES")
                break
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()