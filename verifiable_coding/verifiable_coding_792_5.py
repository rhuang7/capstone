import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        S = data[idx + 1]
        idx += 2
        
        len_S = len(S)
        
        if N < len_S:
            results.append(0)
            continue
        
        # Number of ways to insert len_S characters into N positions
        # = C(N, len_S) * 26^len_S
        # But we need to subtract the cases where the inserted characters are not the same as S
        # Wait, no. The problem is to count the number of strings M of length N such that deleting a substring of M gives S.
        # So M must have S as a subsequence, but not necessarily as a substring.
        # So the problem is to count the number of strings M of length N such that S is a subsequence of M.
        # But the problem says that after deleting a substring of M, the remaining string is S.
        # So M must be of length N, and S must be a subsequence of M.
        # So the problem is to count the number of strings M of length N such that S is a subsequence of M.
        
        # Let's compute the number of such strings.
        # Let's compute the number of ways to insert len_S characters into N positions, such that the inserted characters form S.
        # But this is not correct. We need to count all strings of length N that contain S as a subsequence.
        
        # Let's use dynamic programming.
        # Let dp[i][j] be the number of ways to form a string of length i that contains the first j characters of S as a subsequence.
        # dp[i][j] = dp[i-1][j] * 26 + dp[i-1][j-1]
        # Base case: dp[0][0] = 1, dp[i][0] = 1 for all i.
        
        # But since N can be up to 1e18, we can't compute this directly.
        # We need to find a way to compute this efficiently.
        
        # Let's use matrix exponentiation or find a formula.
        
        # Let's find the number of strings of length N that contain S as a subsequence.
        # Let's use the inclusion-exclusion principle.
        # The total number of strings of length N is 26^N.
        # We subtract the number of strings that do not contain S as a subsequence.
        
        # But how to compute that?
        
        # Let's use the inclusion-exclusion approach.
        # Let's use dynamic programming with matrix exponentiation.
        
        # Let's define dp[i][j] as the number of ways to form a string of length i that contains the first j characters of S as a subsequence.
        # dp[i][j] = dp[i-1][j] * 26 + dp[i-1][j-1]
        # Base case: dp[0][0] = 1, dp[i][0] = 1 for all i.
        
        # We can compute this with matrix exponentiation.
        
        # But since N can be up to 1e18, we need to find a way to compute this efficiently.
        
        # Let's precompute the transitions.
        # The transition matrix is a (len_S + 1) x (len_S + 1) matrix.
        # The transition matrix T is such that T[i][j] = number of ways to go from state i to state j in one step.
        
        # For each state i, the number of ways to stay in state i is 26 (all characters except the one that matches S[i]).
        # The number of ways to go from state i to state i+1 is 1 (the character that matches S[i]).
        
        # So the transition matrix T is:
        # T[i][i] = 25
        # T[i][i+1] = 1
        # All other entries are 0.
        
        # So the initial vector is [1, 0, 0, ..., 0] (length len_S + 1).
        # We need to multiply this vector by T^N to get the final count.
        
        # The answer is dp[N][len_S].
        
        # So we can model this as a matrix exponentiation problem.
        
        # Let's implement matrix exponentiation.
        
        def multiply(A, B):
            res = [[0] * len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                for k in range(len(B)):
                    if A[i][k] == 0:
                        continue
                    for j in range(len(B[0])):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res
        
        def matrix_power(mat, power):
            result = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))]
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result
        
        len_S = len(S)
        if len_S == 0:
            results.append(26 ** N % MOD)
            continue
        
        # Create the transition matrix
        size = len_S + 1
        mat = [[0] * size for _ in range(size)]
        for i in range(size - 1):
            mat[i][i] = 25
            mat[i][i + 1] = 1
        
        # Initial vector is [1, 0, 0, ..., 0]
        # We need to multiply this vector by mat^N
        # The result is a vector, and the answer is the last element of the vector.
        
        mat_pow = matrix_power(mat, N)
        res = 0
        for i in range(size):
            res = (res + mat_pow[i][len_S]) % MOD
        
        results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()