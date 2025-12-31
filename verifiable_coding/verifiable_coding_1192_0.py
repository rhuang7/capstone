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
        
        # Precompute GCDs for all pairs
        gcd_table = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                gcd_table[i][j] = math.gcd(A[i], A[j])
        
        # For each K from 2 to N, find the minimal insertions
        res = []
        for K in range(2, N+1):
            # We need to find the minimal insertions such that no subsequence of length >= K has no consecutive elements with GCD 1
            # This is equivalent to finding the minimal insertions such that the sequence B has no subsequence of length >= K with all consecutive GCDs > 1
            # We can model this as a graph problem where we want to avoid long paths with all edges having GCD > 1
            # We can use BFS to find the minimal insertions to break all such paths of length >= K
            # We need to find the minimal number of insertions such that the graph has no path of length >= K with all edges having GCD > 1
            
            # We can model the problem as finding the minimal number of insertions to break all paths of length >= K in the graph where edges are between nodes with GCD > 1
            # We can use BFS to find the longest path in the graph, and then insert elements to break it
            
            # We will use BFS to find the longest path in the graph where edges are between nodes with GCD > 1
            # We can use dynamic programming to find the longest path in the graph
            # We will use a DP array where dp[i] is the length of the longest path starting at i
            dp = [1] * N
            for i in range(N):
                for j in range(N):
                    if i != j and gcd_table[i][j] > 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
            max_len = max(dp)
            if max_len < K:
                res.append(0)
            else:
                # We need to insert (max_len - K + 1) elements to break all paths of length >= K
                res.append(max_len - K + 1)
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()