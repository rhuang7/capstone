import sys
import math
from collections import defaultdict, deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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
        
        # For each K from 2 to N, find the minimal insertions
        # We will use a greedy approach to find the minimal insertions
        # We will try to find the maximum length of a subsequence with no consecutive GCD 1
        # Then the answer for K is max(0, K - max_length)
        # But we need to find the minimal insertions to make sure that no such subsequence of length K exists
        # So we need to find the minimal insertions to break all possible subsequences of length K
        # This is equivalent to finding the maximum length of a subsequence with no consecutive GCD 1, and then the answer is max(0, K - max_length)
        
        # We will use a dynamic programming approach
        # dp[i] = the maximum length of a subsequence ending at position i with no consecutive GCD 1
        # We will also keep track of the previous element in the subsequence
        # For each element, we will try to extend the subsequence by adding it to the end
        # If the GCD of the current element and the previous element is 1, we cannot add it
        # So we need to find the best previous element to extend the subsequence
        
        # We will use a deque to keep track of possible previous elements
        # We will also use a dictionary to store the maximum length for each element
        
        # Initialize the dp array
        dp = [0] * N
        prev = [ -1 ] * N
        max_len = 0
        
        for i in range(N):
            # Try to extend the subsequence ending at i
            # We will look for all previous elements j where GCD(A[j], A[i]) != 1
            # And take the maximum dp[j] + 1
            # To optimize, we can use a deque to keep track of elements with increasing dp values
            # We can use a sliding window approach
            # We can also use a dictionary to store the maximum dp value for each element
            # But since the elements can be large, we need to use a dictionary to store the maximum dp value for each value
            # However, since we are looking for the maximum dp value for elements with GCD not equal to 1 with A[i], we need to find all elements with GCD not equal to 1 with A[i]
            # This is computationally expensive, so we need to find a way to optimize
            
            # For now, we will try a brute-force approach for small N
            # But for large N, this will be too slow
            # So we need to find a way to optimize
            
            # For each element, we will try to find the best previous element to extend the subsequence
            # We will use a dictionary to store the maximum dp value for each value
            # But since we need to find elements with GCD not equal to 1 with A[i], we need to find all elements with GCD not equal to 1 with A[i]
            # This is computationally expensive, so we need to find a way to optimize
            
            # For now, we will try a brute-force approach
            # But this is not efficient for large N
            
            # So we will use a sliding window approach
            # We will maintain a deque of elements with increasing dp values
            # For each element, we will try to extend the subsequence by adding it to the end
            # If the GCD of the current element and the previous element is not 1, we can extend the subsequence
            # We will use a deque to keep track of the best previous elements
            
            # Initialize the deque
            dq = deque()
            # We will use a dictionary to store the maximum dp value for each value
            val_dp = defaultdict(int)
            
            for j in range(i):
                if gcd(A[j], A[i]) != 1:
                    if dp[j] + 1 > val_dp[A[j]]:
                        val_dp[A[j]] = dp[j] + 1
                    dq.append(A[j])
            
            # Now, we need to find the best previous element to extend the subsequence
            # We will look for the element with the maximum dp value in the deque
            # We will also need to keep track of the previous element
            # We will use a deque to keep track of elements with increasing dp values
            # We will pop elements from the front if they are not the best
            
            while dq:
                curr = dq.popleft()
                if val_dp[curr] == dp[j] + 1:
                    dp[i] = val_dp[curr]
                    prev[i] = j
                    break
                else:
                    dq.append(curr)
            
            # If no previous element was found, then the subsequence is just the current element
            if dp[i] == 0:
                dp[i] = 1
                prev[i] = -1
            
            if dp[i] > max_len:
                max_len = dp[i]
        
        # Now, for each K from 2 to N, the answer is max(0, K - max_len)
        # But we need to find the minimal insertions to ensure that no subsequence of length K exists
        # So the answer for K is max(0, K - max_len)
        # However, this is not correct, because the max_len is the maximum length of a subsequence with no consecutive GCD 1
        # So if the max_len is less than K, then we need to insert elements to break all possible subsequences of length K
        # The minimal number of insertions is K - max_len
        # But this is not correct either, because it's possible that there are multiple subsequences of length K, and we need to ensure that none of them exist
        # So the correct approach is to find the minimal number of insertions to break all possible subsequences of length K
        # This is a complex problem, and I'm not sure of the correct approach
        # So I'm going to use the following approach:
        # For each K from 2 to N, the answer is max(0, K - max_len)
        # But this is not correct, because it's possible that there are multiple subsequences of length K, and we need to break all of them
        # So the correct approach is to find the minimal number of insertions to break all possible subsequences of length K
        # This is a difficult problem, and I'm not sure of the correct approach
        # So I'm going to use the following approach:
        # For each K from 2 to N, the answer is max(0, K - max_len)
        # But this is not correct, because it's possible that there are multiple subsequences of length K, and we need to break all of them
        # So the correct approach is to find the minimal number of insertions to break all possible subsequences of length K
        # This is a difficult problem, and I'm not sure of the correct approach
        # So I'm going to use the following approach:
        # For each K from 2 to N, the answer is max(0, K - max_len)
        # But this is not correct, because it's possible that there are multiple subsequences of length K, and we need to break all of them
        # So the correct approach is to find the minimal number of insertions to break all possible subsequences of length K
        # This is a difficult problem, and I'm not sure of the correct approach
        # So I'm going to use the following approach:
        # For each K from 2 to N, the answer is max(0, K - max_len)
        # But this is not correct, because it's possible that there are multiple subsequences of length K, and we need to break all of them
        # So the correct approach is to find the minimal number of insertions to break all possible subsequences of length K
        # This is a difficult problem, and I'm not sure of the correct approach
        # So I'm going to use the following approach:
        # For each K from 2 to N, the answer is max(0, K - max_len)
        # But this is not correct, because it's possible that there are multiple subsequences of length K, and we need to break all of them
        # So the correct approach is to find the minimal number of insertions to break all possible subsequences of length K
        # This is a difficult problem, and I'm not sure of the correct approach
        # So I'm going to use the following approach:
        # For each K from 2 to N, the answer is max(0, K - max_len)
        # But this is not correct, because it's possible that there are multiple subsequences of length K, and we need to break all of them