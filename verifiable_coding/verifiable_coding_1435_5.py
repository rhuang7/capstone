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
    best_A = []
    best_B = []
    
    for i in range(N):
        for j in range(N):
            len_sub = 0
            for k in range(N - max(N - i, N - j)):
                if i + k < N and j + k < N:
                    if k == 0:
                        diff_A = A[i]
                        diff_B = B[j]
                    else:
                        diff_A = A[i + k] - A[i + k - 1]
                        diff_B = B[j + k] - B[j + k - 1]
                    if diff_A == diff_B:
                        len_sub += 1
                    else:
                        break
            if len_sub > max_len:
                max_len = len_sub
                best_A = A[i:i+max_len]
                best_B = B[j:j+max_len]
    
    print(max_len)
    print(' '.join(map(str, best_A)))
    print(' '.join(map(str, best_B)))

if __name__ == '__main__':
    solve()