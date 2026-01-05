import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        
        # Calculate the product of M^i for i in 1..N
        # But since N can be up to 1e9, we need to compute this efficiently using modular exponentiation
        # However, since M can be up to 1e14, we need to compute M^1 * M^2 * ... * M^N mod MOD
        # This is equivalent to M^(1+2+...+N) mod MOD
        # Sum 1+2+...+N = N*(N+1)//2
        exponent = N * (N + 1) // 2
        result = pow(M, exponent, MOD)
        print(result)

if __name__ == '__main__':
    solve()