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
        for x in range(1, int(math.isqrt(N)) + 1):
            for y in range(1, int(math.isqrt(N)) + 1):
                if x * y <= N:
                    res += 1
        return res
    
    for N in N_list:
        print(count_rectangles(N) % MOD)

if __name__ == '__main__':
    solve()