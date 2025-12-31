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
        K = int(data[idx+1])
        M = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # For each position i (1-based), determine which residue mod M is allowed
        # For position i, required residue is i % M
        # So for each element in A, check if A[j] % M == (pos) % M, where pos is the position in the subsequence
        # We need to count how many elements are valid for each position in the subsequence
        
        # We'll use dynamic programming to count the number of ways to form a subsequence of length k with the required residues
        # dp[k][r] = number of subsequences of length k ending with residue r
        
        # Initialize dp[0][0] = 1 (empty subsequence)
        dp = [{} for _ in range(K+1)]
        dp[0][0] = 1
        
        for i in range(N):
            a = A[i]
            rem = a % M
            for k in range(K, 0, -1):
                # For each position k in the subsequence, we can add this element if it matches the required residue
                required_rem = k % M
                if rem == required_rem:
                    # We can add this element to subsequences of length k-1 ending with any residue
                    for r in dp[k-1]:
                        dp[k][r] = (dp[k][r] + dp[k-1][r]) % MOD
        
        # Sum all possible residues for subsequences of length K
        result = sum(dp[K].values()) % MOD
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()