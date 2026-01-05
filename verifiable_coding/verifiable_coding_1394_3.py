import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    def count_rectangles(N):
        if N == 0:
            return 0
        res = 0
        for i in range(1, int(math.isqrt(N)) + 1):
            j = N // i
            res += j
            if i != j:
                res += j
        return res
    
    for N in N_list:
        print(count_rectangles(N) % MOD)

if __name__ == '__main__':
    solve()