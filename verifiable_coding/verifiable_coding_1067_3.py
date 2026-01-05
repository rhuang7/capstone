import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    N_list = list(map(int, data[1:T+1]))
    
    # Precompute for all N up to 1e18 using matrix exponentiation
    # We can derive the recurrence relation
    # Let f(n) be the number of ways to tile a strip of length n
    # We can derive that f(n) = 2*f(n-1) + 2*f(n-2)
    # Base cases:
    # f(1) = 2 (R1, B1)
    # f(2) = 6 (as given in sample)
    
    # Use matrix exponentiation to compute f(n) efficiently for large n
    
    def multiply(a, b):
        return [
            [ (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD ],
            [ (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD ]
        ]
    
    def matrix_pow(mat, power):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while power > 0:
            if power % 2 == 1:
                result = multiply(result, mat)
            mat = multiply(mat, mat)
            power //= 2
        return result
    
    def compute_f(n):
        if n == 1:
            return 2
        if n == 2:
            return 6
        # Transition matrix for recurrence f(n) = 2*f(n-1) + 2*f(n-2)
        trans = [[2, 2], [1, 0]]
        # Initial vector [f(2), f(1)] = [6, 2]
        # We need to compute trans^(n-2) * [f(2), f(1)]^T
        mat = matrix_pow(trans, n-2)
        return (mat[0][0] * 6 + mat[0][1] * 2) % MOD
    
    for n in N_list:
        print(compute_f(n))

if __name__ == '__main__':
    solve()