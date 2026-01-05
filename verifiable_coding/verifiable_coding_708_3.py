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
            if step == 1:
                p = A
            else:
                p = (product * pow(A, step - 1, MOD)) % MOD
            result = (result + p) % MOD
            product = (product * pow(A, step, MOD)) % MOD
        
        print(result % MOD)

if __name__ == '__main__':
    solve()