import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        A = int(data[index+1])
        index += 2
        
        res = 0
        product = 1
        for i in range(1, N+1):
            step = 2 * i - 1
            res = (res + product * step) % MOD
            product = (product * pow(A, step, MOD)) % MOD
        
        print(res % MOD)

if __name__ == '__main__':
    solve()