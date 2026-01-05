import sys
import math

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
        if N == 0:
            results.append("-1")
            continue
        gcd_val = A[0]
        for num in A[1:]:
            gcd_val = math.gcd(gcd_val, num)
            if gcd_val == 1:
                break
        if gcd_val == 1:
            results.append("-1")
        else:
            results.append(str(gcd_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()