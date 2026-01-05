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
            len_ = 0
            a = A[i]
            b = B[j]
            while len_ < N - max(len(i, j), N - len_ - 1):
                if len_ == 0:
                    diff_A = a
                    diff_B = b
                else:
                    diff_A = A[i + len_] - a
                    diff_B = B[j + len_] - b
                if diff_A == diff_B:
                    len_ += 1
                    a = A[i + len_ - 1]
                    b = B[j + len_ - 1]
                else:
                    break
            if len_ > max_len:
                max_len = len_
                best_A = A[i:i+max_len]
                best_B = B[j:j+max_len]
    
    print(max_len)
    print(' '.join(map(str, best_A)))
    print(' '.join(map(str, best_B)))

if __name__ == '__main__':
    solve()