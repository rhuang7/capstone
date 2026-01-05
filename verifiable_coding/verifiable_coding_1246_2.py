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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_A = max(A)
        max_B = max(B)
        
        if max_B > max_A:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()