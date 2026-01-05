import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute prefix sums of A
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        
        # Precompute prefix sums of B
        # B[i][j] = A[i] + A[j]
        # Sum of square submatrix from (x1, y1) to (x2, y2) is sum_{i=x1}^{x2} sum_{j=y1}^{y2} (A[i] + A[j])
        # = sum_{i=x1}^{x2} (A[i]*(y2 - y1 + 1) + sum_{j=y1}^{y2} A[j])
        # = (y2 - y1 + 1) * sum_{i=x1}^{x2} A[i] + (x2 - x1 + 1) * sum_{j=y1}^{y2} A[j]
        # = (y2 - y1 + 1) * (prefix[x2] - prefix[x1-1]) + (x2 - x1 + 1) * (prefix[y2] - prefix[y1-1])
        
        # Let k = x2 - x1 = y2 - y1
        # Then x2 = x1 + k, y2 = y1 + k
        # So the sum is k * (prefix[x1 + k] - prefix[x1-1]) + (k + 1) * (prefix[y1 + k] - prefix[y1-1])
        # We need this sum to be X
        
        count = 0
        for k in range(1, N+1):
            # For each possible k, iterate over possible x1 and y1
            # x1 can range from 1 to N - k + 1
            # y1 can range from 1 to N - k + 1
            for x1 in range(1, N - k + 2):
                x2 = x1 + k
                sum_x = prefix[x2] - prefix[x1-1]
                term1 = k * sum_x
                # Now find y1 such that (k + 1) * (prefix[y1 + k] - prefix[y1-1]) = X - term1
                # So (prefix[y1 + k] - prefix[y1-1]) = (X - term1) / (k + 1)
                # We need to check if (X - term1) is divisible by (k + 1), and if so, check how many y1 satisfy this
                target = X - term1
                if target < 0:
                    continue
                if target % (k + 1) != 0:
                    continue
                target_val = target // (k + 1)
                # Now find the number of y1 such that prefix[y1 + k] - prefix[y1-1] = target_val
                # This is the same as finding the number of y1 in [1, N - k + 1] such that prefix[y1 + k] - prefix[y1-1] = target_val
                # We can precompute all possible values of prefix[y + k] - prefix[y-1] for y in 1..N-k+1
                # But since k is fixed, we can compute it on the fly
                # So for each y1 in 1..N - k + 1:
                # check if prefix[y1 + k] - prefix[y1-1] == target_val
                # Count how many such y1 exist
                # To make this efficient, we can precompute all possible values of prefix[y + k] - prefix[y-1] for y in 1..N-k+1
                # and use a frequency map
                # But for now, let's do it naively for small k
                # However, for large k, this is O(N^2), which is not feasible
                # So we need a better way
                # We can precompute for all possible k, the values of prefix[y + k] - prefix[y-1] for y in 1..N-k+1
                # and store them in a dictionary
                # But for now, let's proceed with the naive approach
                # This is O(N^2), which is not feasible for N up to 1e5
                # So we need to optimize
                # Let's precompute for all possible k, the values of prefix[y + k] - prefix[y-1] for y in 1..N-k+1
                # and store them in a dictionary
                # Then, for each k, we can check how many times target_val appears in this dictionary
                # This is O(N) per test case
                # So let's precompute for all k
                # But since k can be up to N, and N is up to 1e5, this would be O(N^2), which is not feasible
                # So we need to find another way
                # Let's think differently
                # The sum of the square submatrix is k * sum_x + (k + 1) * sum_y
                # where sum_x is sum of A[i] from x1 to x2, and sum_y is sum of A[j] from y1 to y2
                # We need k * sum_x + (k + 1) * sum_y = X
                # Let's rearrange:
                # (k + 1) * sum_y = X - k * sum_x
                # sum_y = (X - k * sum_x) / (k + 1)
                # We need sum_y to be an integer
                # So for each x1, compute sum_x, then check if (X - k * sum_x) is divisible by (k + 1)
                # If yes, then compute sum_y and count the number of y1 such that sum_y is equal to that value
                # But how to count the number of y1 such that sum_y is equal to a certain value?
                # We can precompute a frequency map of all possible sum_y for all possible y1 and k
                # But since k varies, it's not feasible
                # So let's precompute for all possible k, the frequency map of sum_y
                # But this is O(N^2), which is not feasible
                # So we need to find a way to compute this efficiently
                # Let's think about the possible values of sum_y
                # sum_y is the sum of A[j] from y1 to y1 + k
                # So for each k, sum_y is the sum of a subarray of length k
                # So for each k, we can precompute all possible subarray sums of length k
                # Then, for each x1, compute sum_x and check if (X - k * sum_x) is divisible by (k + 1)
                # If yes, then look up how many times (X - k * sum_x) / (k + 1) appears in the precomputed subarray sums of length k
                # This would be O(N) per test case
                # So let's proceed with this approach
                # Precompute for all possible k, the frequency map of subarray sums of length k
                # We can do this with a sliding window
                # For each k, we can compute the subarray sums of length k and store their frequency
                # Then, for each x1, compute sum_x and check if (X - k * sum_x) is divisible by (k + 1)
                # If yes, then look up the frequency of (X - k * sum_x) / (k + 1) in the frequency map for k
                # This is O(N) per test case
                # So let's proceed
                # First, precompute for all possible k, the frequency map of subarray sums of length k
                # We can do this with a sliding window
                # But since k can be up to N, and N is up to 1e5, this would be O(N^2), which is not feasible
                # So we need to find another way
                # Let's think about the possible values of k
                # For a given k, the number of possible subarrays of length k is N - k + 1
                # So for each k, we can compute the subarray sums of length k and store their frequency
                # Then, for each x1, compute sum_x and check if (X - k * sum_x) is divisible by (k + 1)
                # If yes, then look up the frequency of (X - k * sum_x) / (k + 1) in the frequency map for k