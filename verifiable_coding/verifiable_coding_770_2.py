import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Separate even and odd numbers
        evens = []
        odds = []
        for i in range(n):
            if a[i] % 2 == 0:
                evens.append(a[i])
            else:
                odds.append(a[i])
        
        # Function to find maximum sum of elements with at most K distance between any two
        def max_sum(arr, K):
            # We can take at most one element from each window of size K+1
            # So we can use a sliding window approach to select the maximum elements
            # But since we want the maximum sum, we can greedily take the maximum in each window
            # However, since we can take multiple elements as long as they are not within K distance,
            # We can use dynamic programming
            # Let dp[i] be the maximum sum up to index i
            # We can take a[i] or not take it
            # If we take it, we need to make sure that the previous taken element is at least K+1 away
            # So we can keep track of the last taken index
            # But for efficiency, we can use a sliding window approach
            # Let's use a sliding window approach where we keep track of the maximum in the window
            # We can take the maximum in each window of size K+1
            # But we can't take more than one element from each window
            # So we can use a greedy approach: take the maximum in each window
            # But we need to make sure that we don't take more than one element from each window
            # So we can iterate through the array and whenever we take an element, we skip the next K elements
            # This is a greedy approach
            # But since the array is sorted, we can take the maximum elements
            # Wait, no. The array is not sorted. So we need to find the maximum sum of elements such that no two are within K distance
            # This is similar to the problem of selecting maximum sum with no two elements within K distance
            # Which can be solved with dynamic programming
            # Let dp[i] be the maximum sum up to index i
            # We can take a[i] or not take it
            # If we take a[i], we need to find the last index j where j < i - K, and take dp[j]
            # So dp[i] = max(dp[i-1], a[i] + dp[j])
            # But this is O(n^2), which is not feasible for n up to 1e5
            # So we need a more efficient approach
            # Let's try a greedy approach: take the maximum elements, but skip the next K elements
            # This is not optimal, but it's a possible approach
            # However, the correct approach is to use dynamic programming with a sliding window
            # Let's use a dynamic programming approach
            # Let dp[i] be the maximum sum up to index i
            # We can take a[i] or not take it
            # If we take a[i], we need to find the last index j where j < i - K, and take dp[j]
            # So dp[i] = max(dp[i-1], a[i] + dp[j])
            # But to find j efficiently, we can use a sliding window maximum
            # Let's use a sliding window maximum to find the best j for each i
            # We can use a deque to maintain the indices of the dp array in a way that the maximum is at the front
            # So the dp array is built as follows:
            # dp[0] = a[0]
            # dp[i] = max(dp[i-1], a[i] + max(dp[j] for j in [0, i-K-1]))
            # But for large K, this is not efficient
            # So we can use a sliding window maximum with a deque
            # Let's proceed with this approach
            # Initialize dp array
            dp = [0] * n
            dp[0] = a[0]
            # Use a deque to maintain the indices of the dp array in a way that the maximum is at the front
            from collections import deque
            q = deque()
            q.append(0)
            for i in range(1, n):
                # Remove elements from the front of the deque that are out of the window
                while q and q[0] < i - K - 1:
                    q.popleft()
                # Update dp[i]
                dp[i] = max(dp[i-1], a[i] + (dp[q[0]] if q else 0))
                # Maintain the deque
                while q and dp[i] >= dp[q[-1]]:
                    q.pop()
                q.append(i)
            return dp[-1]
        
        # Now, we need to select elements from even and odd arrays such that no two even are within K distance and no two odd are within K distance
        # So we can take the maximum sum from even and odd arrays, but we have to ensure that the selected elements from even and odd are not within K distance of each other
        # So we can use a dynamic programming approach where we track the last even and last odd index
        # But this is complex
        # Alternative approach: we can take the maximum sum from even and odd arrays, but we have to make sure that the last even and last odd are not within K distance
        # So we can take the maximum sum from even and odd arrays, and then check if the last even and last odd are within K distance
        # If they are, we have to choose between the two
        # But this is not optimal
        # So the correct approach is to use dynamic programming where we track the last even and last odd index
        # Let's proceed with this approach
        # We can use a dynamic programming approach where we track the last even and last odd index
        # Let dp[i] be the maximum sum up to index i
        # We can take a[i] or not take it
        # If we take a[i], we need to check if it's even or odd
        # If it's even, we need to make sure that the last even is at least K+1 away
        # If it's odd, we need to make sure that the last odd is at least K+1 away
        # So we can track the last even and last odd index
        # Let's use a dynamic programming approach where we track the last even and last odd index
        # Let dp[i] be the maximum sum up to index i
        # We can take a[i] or not take it
        # If we take a[i], we need to check if it's even or odd
        # If it's even, we need to make sure that the last even is at least K+1 away
        # If it's odd, we need to make sure that the last odd is at least K+1 away
        # So we can track the last even and last odd index
        # Let's proceed with this approach
        # Initialize dp array
        dp = [0] * n
        last_even = -1
        last_odd = -1
        dp[0] = a[0]
        last_even = 0 if a[0] % 2 == 0 else -1
        last_odd = 0 if a[0] % 2 == 1 else -1
        for i in range(1, n):
            # Option 1: don't take a[i]
            option1 = dp[i-1]
            # Option 2: take a[i]
            option2 = 0
            if a[i] % 2 == 0:
                # Check if last even is at least K+1 away
                if last_even == -1 or i - last_even > K:
                    option2 = dp[i-1] + a[i]
                    last_even = i
                else:
                    # We can't take this even, so we have to take the maximum of the previous dp without this even
                    # But we have to make sure that the last even is not within K distance
                    # So we have to find the maximum dp[j] where j < i - K - 1
                    # This is the same as the previous problem
                    # So we can use the sliding window maximum approach
                    # But for this, we can use the previous function
                    # So we can call the max_sum function on the even array
                    # But we need to find the maximum sum of even elements such that no two are within K distance
                    # Similarly for odd
                    # So we can precompute the max even sum and max odd sum
                    # But we need to make sure that the last even and last odd are not within K distance
                    # So the maximum sum is the maximum of:
                    # max_even_sum + max_odd_sum, if the last even and last odd are not within K