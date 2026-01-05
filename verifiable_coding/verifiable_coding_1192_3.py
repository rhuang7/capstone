import sys
import math
from collections import defaultdict, deque

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
        
        # For each K from 2 to N, find the minimal number of insertions
        # We'll use a sliding window approach to find the maximum length of a subsequence
        # with no consecutive elements having GCD 1
        # The minimal insertions is N - max_length
        
        # We'll use a sliding window approach to find the maximum length of a subsequence
        # with no consecutive elements having GCD 1
        # The maximum length of such a subsequence is the maximum number of elements we can have
        # without violating the condition, so the minimal insertions is N - max_length
        
        # We'll use a sliding window approach to find the maximum length of a subsequence
        # with no consecutive elements having GCD 1
        # We'll use a deque to keep track of the current window
        
        max_len = 0
        dq = deque()
        
        for num in A:
            # Remove elements from the front of the deque if they form a GCD 1 with the current number
            while dq and math.gcd(dq[0], num) == 1:
                dq.popleft()
            # Add the current number to the deque
            dq.append(num)
            # Update the maximum length
            max_len = max(max_len, len(dq))
        
        # For each K from 2 to N, the answer is N - max_len if K <= max_len
        # Otherwise, it's 0 (since we can have a subsequence of length K without any consecutive GCD 1 pairs)
        # But we need to find the minimal insertions for each K from 2 to N
        
        # We'll precompute the answer for each K from 2 to N
        ans = []
        for K in range(2, N+1):
            if K <= max_len:
                ans.append(N - max_len)
            else:
                ans.append(0)
        
        results.append(' '.join(map(str, ans)))
    
    print('\n'.join(results))