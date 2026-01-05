import sys
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
        p = 1
        for i in range(1, N+1):
            step = 2 * i - 1
            res = (res + p * A) % MOD
            p = (p * pow(A, step, MOD)) % MOD
        
        print(res % MOD)

if __name__ == '__main__':
    solve()