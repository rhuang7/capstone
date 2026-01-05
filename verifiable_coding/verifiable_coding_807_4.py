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
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for _ in range(M):
            p = int(data[idx])
            queries.append(p)
            idx += 1
        # Precompute all subarrays and their max elements
        # Since N can be up to 1e5, we need an efficient approach
        # The maximum element in a subarray is the maximum of the elements in that subarray
        # So we need to find the p-th subarray in the sorted list of all subarrays (sorted by their max element)
        # But we can't generate all subarrays, so we need to find the p-th subarray in the sorted list of all subarrays
        # The key insight is that the p-th subarray in the sorted list is the one with the p-th largest maximum element
        # So we can find the p-th largest maximum element
        # We can use a max-heap to find the p-th largest maximum element
        # However, since the subarrays are sorted in descending order of their max elements, we can use a max-heap
        # But since we need to find the p-th subarray, we need to find the p-th largest maximum element
        # So we can use a max-heap to find the p-th largest maximum element
        # But for large N, we need an efficient way to find the p-th largest maximum element
        # The maximum element in the array is the maximum of the entire array
        # The second maximum is the maximum of the array excluding the maximum element
        # But this approach is not efficient for large N
        # So we can use a selection algorithm to find the p-th largest maximum element
        # However, for this problem, we can use a binary search approach
        # Let's find the p-th largest maximum element
        # We can use binary search on the value of the maximum element
        # The maximum possible value is 1e9
        # The minimum possible value is 1
        # For each candidate value, we can count how many subarrays have maximum element >= candidate
        # If the count is >= p, then the answer is >= candidate
        # Else, the answer is < candidate
        # So we can perform binary search on the value of the maximum element
        # Now, we need to implement the count function
        # The count function: given a value x, how many subarrays have maximum element >= x
        # To compute this, we can use a sliding window approach
        # For each element, we can find the number of subarrays where the maximum element is >= x
        # This is similar to the problem of finding the number of subarrays with maximum >= x
        # We can use a sliding window approach to find the number of subarrays with maximum >= x
        # So the count function is:
        def count(x):
            # Count the number of subarrays with maximum element >= x
            # We can use a sliding window approach
            # We can use a deque to keep track of the maximum elements in the current window
            # Initialize left = 0, right = 0
            # We can iterate through the array and for each right, we can expand the window
            # We can maintain a deque that stores indices of elements in the current window in decreasing order
            # For each right, we add A[right] to the deque, removing all elements smaller than A[right]
            # Then, while the front of the deque is less than x, we remove it from the deque and increment left
            # The number of subarrays ending at right with maximum >= x is right - left + 1
            # So we can accumulate this count
            # But this approach is O(N) for each x
            # However, since we are doing binary search, this is acceptable
            # Let's implement this
            left = 0
            dq = []
            count = 0
            for right in range(N):
                # Maintain the deque in decreasing order
                while dq and A[dq[-1]] < A[right]:
                    dq.pop()
                dq.append(right)
                # Remove elements from the front that are less than x
                while dq and A[dq[0]] < x:
                    dq.popleft()
                    left += 1
                # The number of subarrays ending at right with maximum >= x is right - left + 1
                count += right - left + 1
            return count
        # Now perform binary search on the value of the maximum element
        low = 1
        high = 10**9
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            c = count(mid)
            if c >= p:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        results.append(str(answer))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()