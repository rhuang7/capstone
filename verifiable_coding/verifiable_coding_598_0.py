import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    if K == 0:
        print(' '.join(map(str, A)))
        return
    
    max_val = max(A)
    for i in range(N):
        A[i] = max_val - A[i]
    
    if K % 2 == 0:
        print(' '.join(map(str, A)))
    else:
        max_val = max(A)
        for i in range(N):
            A[i] = max_val - A[i]
        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()