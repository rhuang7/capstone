import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ns = list(map(int, data[1:]))
    
    # Precompute for all N up to 1e18 using matrix exponentiation
    # But since N can be up to 1e18, we need a fast way to compute the recurrence
    # Let's find the recurrence relation
    
    # Let dp[n] be the number of ways to tile a strip of length n
    # For n = 1: 2 ways (R1, B1)
    # For n = 2: 6 ways (RR, RB, BR, BB, R2, B2)
    # We can find the recurrence by considering the last step
    # dp[n] = 2 * dp[n-1] + 2 * dp[n-2]
    # Because:
    # - Add a 1-unit tile (R or B) to a tiling of n-1: 2 * dp[n-1]
    # - Add a 2-unit tile (R or B) to a tiling of n-2: 2 * dp[n-2]
    
    # Now we can use matrix exponentiation to compute dp[n] efficiently for large n
    
    def matrix_mult(a, b):
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
                result = matrix_mult(result, mat)
            mat = matrix_mult(mat, mat)
            power //= 2
        return result
    
    def compute_dp(n):
        if n == 0:
            return 1
        if n == 1:
            return 2
        # Transition matrix for recurrence dp[n] = 2*dp[n-1] + 2*dp[n-2]
        # [[2, 2], [1, 0]]
        trans = [[2, 2], [1, 0]]
        mat = matrix_pow(trans, n-1)
        return (mat[0][0] * 2 + mat[0][1] * 1) % MOD
    
    for n in Ns:
        print(compute_dp(n))

if __name__ == '__main__':
    solve()