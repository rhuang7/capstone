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
            for k in range(N):
                for l in range(k + 1, N):
                    subA = A[i:j]
                    subB = B[k:l]
                    if len(subA) == len(subB):
                        diffA = [subA[m+1] - subA[m] for m in range(len(subA)-1)]
                        diffB = [subB[m+1] - subB[m] for m in range(len(subB)-1)]
                        if diffA == diffB:
                            if len(subA) > max_len:
                                max_len = len(subA)
                                best_subA = subA
                                best_subB = subB
    print(max_len)
    print(' '.join(map(str, best_subA)))
    print(' '.join(map(str, best_subB)))

if __name__ == '__main__':
    solve()