import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return math.comb(n, k)
    
    def solve_for_N(N):
        if N == 2:
            return 0
        total = 0
        for i in range(1, N):
            for j in range(1, N - i):
                if (i + j) % 2 == 1:
                    total += 1
        return total
    
    results = []
    for N in Ns:
        res = solve_for_N(N)
        results.append(res)
    
    for res in results:
        print(res % MOD)

if __name__ == '__main__':
    solve()