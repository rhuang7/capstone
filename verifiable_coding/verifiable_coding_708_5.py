import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        A = int(data[idx+1])
        idx += 2
        
        res = 0
        prod = 1
        for i in range(1, N+1):
            step = 2 * i - 1
            if step > N:
                break
            count = step
            if count > N:
                count = N
            if count % 2 == 0:
                count -= 1
            if count > N:
                count = N
            if count == 0:
                break
            res = (res + prod * pow(A, count, MOD)) % MOD
            prod = (prod * pow(A, count, MOD)) % MOD
        
        print(res % MOD)

if __name__ == '__main__':
    solve()