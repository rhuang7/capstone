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
            len_a = 0
            len_b = 0
            for k in range(N):
                if i + k >= N or j + k >= N:
                    break
                if k == 0:
                    diff_a = A[i + k] - A[i + k - 1]
                    diff_b = B[j + k] - B[j + k - 1]
                else:
                    diff_a = A[i + k] - A[i + k - 1]
                    diff_b = B[j + k] - B[j + k - 1]
                if diff_a != diff_b:
                    break
                len_a += 1
                len_b += 1
            if len_a > max_len:
                max_len = len_a
                best_A = A[i:i+max_len]
                best_B = B[j:j+max_len]
    
    print(max_len)
    print(' '.join(map(str, best_A)))
    print(' '.join(map(str, best_B)))

if __name__ == '__main__':
    solve()