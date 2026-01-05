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
            while len_ < N - max(len(i, j), N - i, N - j):
                if len_ == 0:
                    diff_a = 0
                    diff_b = 0
                else:
                    diff_a = A[i + len_] - A[i + len_ - 1]
                    diff_b = B[j + len_] - B[j + len_ - 1]
                if diff_a != diff_b:
                    break
                len_ += 1
            if len_ > max_len:
                max_len = len_
                best_A = A[i:i+len_]
                best_B = B[j:j+len_]
    
    print(max_len)
    print(' '.join(map(str, best_A)))
    print(' '.join(map(str, best_B)))

if __name__ == '__main__':
    solve()