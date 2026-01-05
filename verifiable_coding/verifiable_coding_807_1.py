import sys

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
            queries.append(int(data[idx]))
            idx += 1
        # Precompute all subarrays and their max elements
        # Since N can be up to 1e5, we need an efficient way
        # We'll use the fact that the pth subarray is the pth in the sorted list of all subarrays
        # When sorted in descending order, the first subarray is the entire array, the second is the array without the last element, etc.
        # But we need to sort all subarrays in the compare function
        # Instead of generating all subarrays, we can find the pth subarray in the sorted list
        # The key insight is that the pth subarray in the sorted list is the one with the largest possible maximum element
        # So for each query p, we need to find the subarray that is the pth in the sorted list
        # We can use a binary search approach to find the maximum element
        # We'll use a binary search on the possible maximum elements
        # For a given value x, we can count how many subarrays have maximum element >= x
        # This can be done efficiently using a sliding window approach
        # We'll precompute for each possible x the number of subarrays with max >= x
        # Then perform binary search on x to find the maximum x such that the count is >= p
        # To handle large N (up to 1e5), we need an O(N log N) solution
        # Let's precompute the sorted list of all elements
        sorted_A = sorted(A)
        # Binary search on the possible maximum elements
        low = 1
        high = max(A)
        # Precompute the frequency of each element
        freq = {}
        for num in A:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # Function to count the number of subarrays with max >= x
        def count_subarrays(x):
            count = 0
            # We need to find the number of subarrays where the maximum element is >= x
            # We can use a sliding window approach
            # For each right, find the leftmost index where the max in the window is >= x
            # We can use a deque to track the max in the window
            from collections import deque
            dq = deque()
            left = 0
            for right in range(N):
                while dq and A[right] > A[dq[-1]]:
                    dq.pop()
                dq.append(right)
                # Remove elements from the front that are out of the window
                while dq[0] < left:
                    dq.popleft()
                # If the max in the window is >= x, then all subarrays ending at right and starting at left to dq[0] are valid
                if A[dq[0]] >= x:
                    count += right - left + 1
                else:
                    # Move left to the right until the max is >= x
                    while left <= right and A[dq[0]] < x:
                        left += 1
            return count
        # Binary search for the maximum x such that count_subarrays(x) >= p
        for p in queries:
            low = 1
            high = max(A)
            answer = 1
            while low <= high:
                mid = (low + high) // 2
                cnt = count_subarrays(mid)
                if cnt >= p:
                    answer = mid
                    low = mid + 1
                else:
                    high = mid - 1
            results.append(str(answer))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()