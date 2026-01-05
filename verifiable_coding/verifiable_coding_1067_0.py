import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    # Precompute for all N up to 1e18 using matrix exponentiation
    # The recurrence is f(n) = 2*f(n-1) + 2*f(n-2)
    # Because:
    # - 2 ways to place a red or blue 1x1 tile on the first position, then f(n-1)
    # - 2 ways to place a red or blue 2x1 tile on the first two positions, then f(n-2)
    
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
        if n == 0:
            return 1
        if n == 1:
            return 2
        mat = [[2, 2], [1, 1]]
        power = n - 2
        mat_pow = matrix_pow(mat, power)
        return (mat_pow[0][0] * 2 + mat_pow[0][1] * 1) % MOD
    
    for N in N_list:
        print(fast_exponentiation(N))

if __name__ == '__main__':
    solve()