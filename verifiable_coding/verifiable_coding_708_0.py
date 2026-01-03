import sys
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
        
        result = 0
        product = 1
        for i in range(1, N+1):
            step = 2 * i - 1
            current_product = pow(A, step, MOD)
            result = (result + current_product) % MOD
            product = (product * current_product) % MOD
        
        print(result % MOD)

if __name__ == '__main__':
    solve()