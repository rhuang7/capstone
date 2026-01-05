import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    A = list(map(int, input[idx:idx+N]))
    idx += N
    B = list(map(int, input[idx:idx+N]))
    
    max_len = 0
    best_subA = []
    best_subB = []
    
    for i in range(N):
        for j in range(i + 1, N):
            diffA = []
            diffB = []
            for k in range(i, j):
                if k + 1 < j:
                    diffA.append(A[k+1] - A[k])
                    diffB.append(B[k+1] - B[k])
            if len(diffA) == len(diffB):
                if len(diffA) > max_len:
                    max_len = len(diffA)
                    best_subA = A[i:j+1]
                    best_subB = B[i:j+1]
    
    print(max_len)
    print(' '.join(map(str, best_subA)))
    print(' '.join(map(str, best_subB)))

if __name__ == '__main__':
    solve()