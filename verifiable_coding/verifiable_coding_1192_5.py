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
        
        # For each K from 2 to N, find the minimal number of insertions
        # We need to find the minimal number of insertions such that there is no subsequence of length K with no consecutive pair having GCD 1
        # This is equivalent to ensuring that the sequence B has a subsequence of length K with at least one pair of consecutive elements with GCD 1
        
        # We can model this as trying to find the longest possible sequence of elements in A with no consecutive pair having GCD 1
        # Then, the minimal number of insertions is max(0, K - length_of_longest_sequence)
        
        # Let's find the longest sequence of elements in A with no consecutive pair having GCD 1
        # We can use dynamic programming for this
        
        # dp[i] = length of the longest sequence ending at index i with no consecutive pair having GCD 1
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if math.gcd(A[i], A[j]) != 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_len = max(dp)
        
        # For each K from 2 to N, the answer is max(0, K - max_len)
        res = []
        for K in range(2, N+1):
            res.append(str(max(0, K - max_len)))
        
        results.append(' '.join(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()