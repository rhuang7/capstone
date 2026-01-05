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
        
        A.sort()
        res = A[0]
        for i in range(1, N):
            res += A[i] // A[i-1] * A[i-1]
        
        results.append(res)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    solve()