import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    for N in N_list:
        if N == 1:
            print(4)
            continue
        if N == 2:
            print(6)
            continue
        
        # Using matrix exponentiation for fast computation
        # Define the recurrence relation
        # Let dp[n] be the number of ways to tile a strip of length n
        # dp[n] = 2 * dp[n-1] + 2 * dp[n-2]
        # Base cases: dp[1] = 4, dp[2] = 6
        
        def multiply(a, b):
            return [
                (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
                (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD,
                (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
                (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD
            ]
        
        def matrix_pow(mat, power):
            result = [1, 0, 0, 1]  # Identity matrix
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result
        
        # Transition matrix for the recurrence dp[n] = 2*dp[n-1] + 2*dp[n-2]
        # The matrix is:
        # [2 2]
        # [1 0]
        # But we need to represent it in a 4x4 matrix for the recurrence
        # Since dp[n] = 2*dp[n-1] + 2*dp[n-2], we can use a 2x2 matrix
        # But for the purposes of this code, we use a 4x4 matrix to represent the recurrence
        # The matrix is:
        # [2 2 0 0]
        # [1 0 0 0]
        # [0 0 1 0]
        # [0 0 0 1]
        # But we can simplify it to a 2x2 matrix for the recurrence
        # So the matrix is:
        # [2 2]
        # [1 0]
        mat = [[2, 2], [1, 0]]
        
        # Compute mat^(n-2)
        mat_pow = matrix_pow(mat, N-2)
        
        # Initial conditions: dp[1] = 4, dp[2] = 6
        # So dp[N] = mat_pow[0][0] * dp[2] + mat_pow[0][1] * dp[1]
        result = (mat_pow[0][0] * 6 + mat_pow[0][1] * 4) % MOD
        print(result)

if __name__ == '__main__':
    solve()