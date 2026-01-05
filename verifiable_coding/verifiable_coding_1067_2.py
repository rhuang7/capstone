import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    # Precompute for all possible N up to 1e18 using matrix exponentiation
    # But since N can be up to 1e18, we need a formula-based approach
    # Let's find a recurrence relation
    
    # Let dp[n] be the number of ways to tile a strip of length n
    # For n = 1: 2 ways (R1, B1)
    # For n = 2: 6 ways (RR, RB, BR, BB, R2, B2)
    # Let's find the recurrence
    # dp[0] = 1 (base case)
    # dp[1] = 2
    # dp[2] = 6
    # For n >= 3:
    # dp[n] = 2 * dp[n-1] + 2 * dp[n-2]
    # Explanation:
    # 2 * dp[n-1]: add a 1-unit tile (R or B) to any tiling of n-1
    # 2 * dp[n-2]: add a 2-unit tile (R or B) to any tiling of n-2
    
    # We can compute this using matrix exponentiation for large n
    
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
        # Transition matrix for the recurrence dp[n] = 2*dp[n-1] + 2*dp[n-2]
        # We use the matrix [[2, 2], [1, 0]] and raise it to (n-2)th power
        mat = [[2, 2], [1, 0]]
        mat_pow = matrix_pow(mat, n-2)
        return (mat_pow[0][0] * 2 + mat_pow[0][1] * 1) % MOD
    
    for n in N_list:
        print(compute_dp(n))
        
if __name__ == '__main__':
    solve()