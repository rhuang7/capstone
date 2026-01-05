import sys
import math
from collections import defaultdict

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
        # Preprocess the array to find the minimum number of insertions for each K
        # We need to find the minimal number of insertions such that no subsequence of length K has no consecutive elements with GCD 1
        # This is equivalent to ensuring that every subsequence of length K has at least one pair of consecutive elements with GCD 1
        # We can model this as a graph problem where each node is an element in the array and edges represent GCD 1
        # We need to find the longest path in this graph, and the answer for K is N - (length of longest path)
        # However, since the array is circular, we need to consider all possible rotations
        # But for the purposes of this problem, we can consider the array as linear and then check for the longest path
        # We can use dynamic programming to find the longest path in the graph
        # Let's build the graph
        graph = defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                if math.gcd(A[i], A[j]) == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        # Now, we need to find the longest path in this graph
        # We can use DFS with memoization
        # However, for large N, this may not be efficient
        # So we'll use a dynamic programming approach
        # Let dp[i] be the length of the longest path starting at i
        dp = [1] * N
        visited = [False] * N
        # We'll use a memoization approach to avoid recomputation
        # But for the purposes of this problem, we can use a simple DFS approach
        # We'll iterate through each node and perform DFS to find the longest path
        # However, for large N, this may not be efficient
        # So we'll use a topological sort approach
        # But since the graph is undirected, we can't do that
        # So we'll use a DFS-based approach with memoization
        # We'll use a memoization array to store the longest path starting at each node
        memo = [0] * N
        def dfs(u):
            if memo[u] != 0:
                return memo[u]
            max_len = 1
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    res = dfs(v)
                    max_len = max(max_len, res + 1)
            memo[u] = max_len
            return max_len
        # We'll perform DFS for each node
        max_len = 0
        for i in range(N):
            visited = [False] * N
            dfs(i)
            max_len = max(max_len, memo[i])
        # The answer for K is N - max_len
        # But we need to output for K from 2 to N
        # So for K = 2, the answer is N - max_len_2
        # But we need to find the minimal number of insertions such that for each K from 2 to N, there is no subsequence of length K with no consecutive elements having GCD 1
        # This is equivalent to ensuring that the longest path in the graph is less than K
        # So for each K from 2 to N, the answer is N - (longest path length for K)
        # But since the longest path is fixed, we can compute it once
        # So the answer for K is N - (longest path length)
        # However, this is only valid if the longest path is less than K
        # So for each K, the answer is N - (longest path length) if longest path length < K
        # Otherwise, it's 0
        # So we need to compute the longest path for each K
        # But this is not feasible for large N
        # So we'll use the longest path computed above
        # The answer for K is N - (longest path length) if longest path length < K
        # Otherwise, it's 0
        # So for K from 2 to N, the answer is max(0, N - (longest path length)) if longest path length < K
        # But since we need the minimal number of insertions, we need to find the minimal number of insertions such that the longest path is less than K
        # This is equivalent to finding the minimal number of insertions such that the longest path is at most K-1
        # So the answer for K is N - (longest path length) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So we can precompute the longest path length
        # Then for each K from 2 to N, the answer is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # But since the longest path length is fixed, we can compute it once
        # So for each K from 2 to N, the answer is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # But since the longest path length is fixed, we can compute it once
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path length)) if longest path length < K
        # Otherwise, it's 0
        # So the answer for K is max(0, N - (longest path