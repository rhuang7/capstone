import sys
import math
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute gcd for all pairs
        gcd_table = [[0] * N for _ in range(N)]
        for i in range(N):
            gcd_table[i][i] = A[i]
            for j in range(i+1, N):
                gcd_table[i][j] = math.gcd(A[i], A[j])
        
        # For each K from 2 to N, find the minimal insertions
        res = []
        for K in range(2, N+1):
            # We need to find the minimal number of insertions such that there is no subsequence of length >= K
            # with no consecutive elements having gcd 1
            # So we need to find the maximum length of a subsequence with no consecutive elements having gcd 1
            # and then the answer is max(0, K - max_length)
            # So we need to find the maximum length of such a subsequence
            # We can use dynamic programming
            # dp[i] = maximum length of such subsequence ending at i
            dp = [1] * N
            for i in range(N):
                for j in range(i):
                    if math.gcd(A[i], A[j]) != 1:
                        dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(dp)
            res.append(max(0, K - max_len))
        
        results.append(res)
    
    for res in results:
        print(' '.join(map(str, res)))

if __name__ == '__main__':
    main()