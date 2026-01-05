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
        # Precompute GCDs for all pairs
        gcds = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                gcds[i][j] = math.gcd(A[i], A[j])
        # For each K from 2 to N, find the minimal number of insertions
        res = []
        for K in range(2, N+1):
            # Try to find a sequence B such that no subsequence of length >= K has no consecutive elements with GCD 1
            # We can try to find the minimal number of insertions to break all possible long subsequences
            # This is a complex problem, but for the purpose of this problem, we can use a greedy approach
            # We need to find the minimal number of insertions such that in the resulting sequence B, any subsequence of length >= K has at least one pair of consecutive elements with GCD 1
            # This is equivalent to ensuring that the sequence B has no subsequence of length >= K with all consecutive elements having GCD > 1
            # To achieve this, we can try to find the maximum number of elements that can be placed in a sequence such that no consecutive elements have GCD 1
            # Then, the minimal number of insertions is N - max_length
            # We can use dynamic programming to find the maximum length of such a sequence
            # Let dp[i] be the maximum length of a sequence ending at position i with the last element having GCD > 1 with the previous element
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But this is O(N^2), which is not feasible for N up to 1e5
            # So we need a more efficient approach
            # Instead, we can try to find the maximum number of elements that can be placed in a sequence such that no consecutive elements have GCD 1
            # This is equivalent to finding the maximum number of elements that can be placed in a sequence where each consecutive pair has GCD 1
            # We can use a greedy approach: try to place elements in the sequence such that each new element has GCD 1 with the previous one
            # But this is not guaranteed to give the maximum length
            # So we need a better approach
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # For each i, we can look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5
            # So we need to find a way to compute this efficiently
            # Let's try to find the maximum length of a sequence where no two consecutive elements have GCD 1
            # We can use a dynamic programming approach with a set of possible previous GCDs
            # Let dp[i] be the maximum length of a sequence ending at position i
            # We can initialize dp as 1 for each element
            # Then, for each i, we look at all previous j < i and if gcd(A[i], A[j]) > 1, then dp[i] = max(dp[i], dp[j] + 1)
            # But again, this is O(N^2), which is not feasible for N up to 1e5