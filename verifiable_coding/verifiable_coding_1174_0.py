import sys
import math
MOD = 10**9 + 7

def count_set_bits(x):
    return bin(x).count('1')

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
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    a = A[i]
                    b = A[j]
                    c = A[k]
                    log_b = math.floor(math.log2(b))
                    log_c = math.floor(math.log2(c))
                    shift1 = log_b + log_c + 2
                    shift2 = log_b + 1
                    P = (a << shift1) + (b << shift2) + c
                    if count_set_bits(P) % 2 == 1:
                        count += 1
        results.append(count % MOD)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()