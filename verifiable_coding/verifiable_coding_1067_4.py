import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    # Precompute results for all N up to 1e18 using matrix exponentiation
    # The recurrence relation is f(n) = 2*f(n-1) + 2*f(n-2)
    # Base cases: f(1) = 2, f(2) = 6
    
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
    
    def fast_exponentiation(n):
        if n == 1:
            return 2
        if n == 2:
            return 6
        mat = [[2, 1], [1, 1]]  # Transition matrix for recurrence f(n) = 2*f(n-1) + 2*f(n-2)
        mat_pow = matrix_pow(mat, n-2)
        return (mat_pow[0][0] * 6 + mat_pow[0][1] * 2) % MOD
    
    for n in N_list:
        print(fast_exponentiation(n))

if __name__ == '__main__':
    solve()