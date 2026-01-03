import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:T+1]))
    
    for N in Ns:
        if N == 1:
            print(4)
            continue
        if N == 2:
            print(6)
            continue
        
        # We can use matrix exponentiation for large N
        # Let dp[n] be the number of ways to tile a strip of length n
        # dp[n] = 2 * dp[n-1] + 2 * dp[n-2]
        # Base cases: dp[0] = 1, dp[1] = 4
        # This recurrence is derived from considering the possible tiles that can be placed at the end
        
        # We'll use fast matrix exponentiation to compute dp[N]
        # The transition matrix is:
        # [1 2]
        # [1 0]
        # Because dp[n] = 2*dp[n-1] + 2*dp[n-2]
        # So the matrix is [[2, 2], [1, 0]] but we need to adjust for the base cases
        
        def multiply(a, b):
            return [
                [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
                 (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
                [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
                 (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]
            ]
        
        def matrix_pow(mat, power):
            result = [[1, 0], [0, 1]]  # Identity matrix
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result
        
        def compute_dp(n):
            if n == 0:
                return 1
            if n == 1:
                return 4
            mat = [[2, 2], [1, 0]]
            mat_pow = matrix_pow(mat, n-2)
            return (mat_pow[0][0] * 4 + mat_pow[0][1] * 1) % MOD
        
        print(compute_dp(N))

if __name__ == '__main__':
    solve()