import sys
import math

def least_prime_divisor(x):
    if x == 1:
        return 1
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return i
    return x

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
        M = int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        output = []
        for _ in range(M):
            type_op = int(data[idx])
            L = int(data[idx+1]) - 1
            R = int(data[idx+2]) - 1
            idx += 3
            if type_op == 0:
                for i in range(L, R+1):
                    x = A[i]
                    lpd = least_prime_divisor(x)
                    A[i] = x // lpd
            else:
                res = 1
                for i in range(L, R+1):
                    x = A[i]
                    lpd = least_prime_divisor(x)
                    res = max(res, lpd)
                output.append(str(res))
        results.append('\n' + ' '.join(output))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()