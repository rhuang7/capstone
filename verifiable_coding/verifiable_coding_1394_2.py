import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    def count_rectangles(n):
        if n == 0:
            return 0
        res = 0
        sqrt_n = int(math.isqrt(n))
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                j = n // i
                res += 2 * (i * j)
                if i != j:
                    res += 1
        return res
    
    for n in N_list:
        print(count_rectangles(n) % MOD)
        
if __name__ == '__main__':
    solve()