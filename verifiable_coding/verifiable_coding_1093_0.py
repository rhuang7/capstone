import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        M = int(data[idx+2])
        idx += 3
        
        product = 1
        for i in range(L-1, R):
            product = (product * A[i]) % M
        
        results.append(str(product))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()