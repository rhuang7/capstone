import sys
import math
from collections import defaultdict

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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        # Precompute gcd for all pairs
        gcd_table = [[0]*(N) for _ in range(N)]
        for i in range(N):
            gcd_table[i][i] = A[i]
            for j in range(i+1, N):
                gcd_table[i][j] = math.gcd(A[i], A[j])
        # For each K from 2 to N, find the minimal insertions
        res = []
        for K in range(2, N+1):
            # We need to find the minimal insertions such that there is no subsequence of length >= K with no consecutive elements having gcd 1
            # This is equivalent to ensuring that every subsequence of length >= K has at least one pair of consecutive elements with gcd 1
            # So we need to find the minimal insertions to make the sequence such that every subsequence of length >= K has at least one such pair
            # This is equivalent to finding the minimal insertions to make the sequence such that the maximum length of a subsequence with no consecutive elements having gcd 1 is < K
            # So we need to find the minimal insertions to make the maximum length of such a subsequence < K
            # This is equivalent to finding the minimal insertions to make the sequence have a maximum length of such a subsequence < K
            # This is a problem of finding the minimal insertions to break all possible sequences of length >= K with no consecutive elements having gcd 1
            # We can model this as a graph problem where each node is a position in the sequence and edges represent consecutive elements with gcd 1
            # We need to find the minimal insertions to break all paths of length >= K in this graph
            # This is equivalent to finding the minimal number of insertions to make the graph have no path of length >= K
            # To do this, we can model it as a dynamic programming problem
            # Let dp[i] be the maximum length of a subsequence ending at position i with no consecutive elements having gcd 1
            # We can compute this using the gcd_table
            dp = [0]*N
            for i in range(N):
                for j in range(i):
                    if gcd_table[i][j] != 1:
                        dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(dp)
            # The minimal insertions needed is (K - 1) - max_len if max_len < K else 0
            # Because if the maximum length is less than K, we need to insert (K - 1 - max_len) elements to make it at least K
            # If it's already >= K, no insertions are needed
            if max_len >= K:
                res.append(0)
            else:
                res.append(K - 1 - max_len)
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))