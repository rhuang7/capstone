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
        gcd_val = A[0]
        for num in A:
            gcd_val = math.gcd(gcd_val, num)
        total = sum(A) // gcd_val
        results.append(f"{gcd_val} {total}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()