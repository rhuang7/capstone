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
        max_x = int(math.isqrt(N))
        res = 0
        for x in range(1, max_x + 1):
            max_y = N // x
            res += max_y
        return res
    
    for N in N_list:
        print(count_rectangles(N) % MOD)

if __name__ == '__main__':
    solve()