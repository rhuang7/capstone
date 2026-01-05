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
        
        # For each position i (1-based), we determine what remainder it should have
        # in the subsequence. For the i-th element in the subsequence, it should be
        # congruent to i mod M.
        # So for each element in the array, we check if it can be part of a subsequence
        # in a certain position.
        
        # We will create a list of counts for each remainder group.
        # For each remainder r (0 <= r < M), we will have a list of counts of elements
        # in the array that satisfy A[i] % M == r.
        # Then, for each position in the subsequence (from 1 to K), we need to choose
        # an element with the correct remainder.
        
        # We will use dynamic programming to count the number of ways to form a subsequence
        # of length k with the first k elements having the correct remainders.
        
        # Initialize dp array where dp[k] is the number of subsequences of length k
        # that satisfy the condition.
        dp = [0] * (K + 1)
        dp[0] = 1  # Base case: one way to choose an empty subsequence
        
        # For each element in the array, we will update the dp array
        for a in A:
            # Compute the remainder of the element
            r = a % M
            # For each position in the subsequence (from K down to 1)
            for k in range(K, 0, -1):
                # The current element can be placed in the k-th position of the subsequence
                # if the remainder matches k % M
                if r == k % M:
                    dp[k] = (dp[k] + dp[k-1]) % MOD
        
        results.append(dp[K] % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()