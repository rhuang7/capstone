import sys
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.isqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        if K == 1:
            if is_prime(N):
                results.append('1')
            else:
                results.append('0')
            continue
        if N < K:
            results.append('0')
            continue
        if K == 2:
            if N >= 2 + 2 and is_prime(N - 2) and is_prime(2):
                results.append('1')
            else:
                results.append('0')
            continue
        if K >= 3:
            if N >= 2 * K and (N - 2 * K) % 2 == 0:
                results.append('1')
            else:
                results.append('0')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()