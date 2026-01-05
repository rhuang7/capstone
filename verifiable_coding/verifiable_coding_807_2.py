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
        # Each subarray is sorted in descending order
        # We need to find the p-th subarray in the sorted list of all subarrays
        # According to the compare function, the subarrays are sorted in descending order
        # So the p-th subarray is the one with the highest value in the compare function
        # The maximum element in the p-th subarray is the maximum element of that subarray
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # and return its maximum element
        # To do this efficiently, we can precompute all subarrays and sort them
        # However, for large N (up to 1e5), this is not feasible
        # So we need a smarter approach
        # The key insight is that the p-th subarray in the sorted list is the one with the largest maximum element
        # So we can find the maximum element in the array and count how many subarrays have that maximum element
        # Then, if p is within that count, the answer is that maximum element
        # Otherwise, we need to find the next maximum element and repeat
        # This is a greedy approach
        # So we can do the following:
        # 1. Find all unique elements in the array
        # 2. Sort them in descending order
        # 3. For each element, count how many subarrays have that element as their maximum
        # 4. Find the smallest element such that the cumulative count is >= p
        # This is the element that is the maximum of the p-th subarray
        # So the answer is that element
        # Now, how to count how many subarrays have a given element as their maximum
        # For a given element x, the number of subarrays where x is the maximum is equal to the number of subarrays where x is the maximum element
        # This can be computed using a monotonic stack approach
        # So the plan is:
        # - Find all unique elements in the array
        # - Sort them in descending order
        # - For each element, compute the number of subarrays where it is the maximum
        # - Use binary search to find the smallest element such that the cumulative count is >= p
        # Now, let's implement this
        # First, find all unique elements in the array
        unique_elements = sorted(set(A), reverse=True)
        # Now, for each element, compute the number of subarrays where it is the maximum
        # We can use a monotonic stack approach
        # For each element, find the number of subarrays where it is the maximum
        # This is a standard problem
        # The number of subarrays where A[i] is the maximum is equal to (i - left[i]) * (right[i] - i)
        # where left[i] is the index of the last element to the left of i that is greater than A[i]
        # and right[i] is the index of the first element to the right of i that is greater than or equal to A[i]
        # So we need to compute left and right arrays
        # Let's compute left and right arrays
        # First, compute left array
        left = [ -1 ] * N
        stack = []
        for i in range(N):
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        # Now compute right array
        right = [ N ] * N
        stack = []
        for i in range(N-1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = N
            stack.append(i)
        # Now compute the number of subarrays where A[i] is the maximum
        count = [ 0 ] * N
        for i in range(N):
            count[i] = (i - left[i]) * (right[i] - i)
        # Now, we need to group the elements by their value and sum their counts
        # We can create a dictionary that maps each value to the total number of subarrays where it is the maximum
        value_counts = {}
        for i in range(N):
            val = A[i]
            if val not in value_counts:
                value_counts[val] = 0
            value_counts[val] += count[i]
        # Now, sort the unique elements in descending order
        sorted_unique = sorted(value_counts.keys(), reverse=True)
        # Now, perform a binary search to find the smallest value such that the cumulative count is >= p
        # We can use a prefix sum array
        prefix = []
        total = 0
        for val in sorted_unique:
            total += value_counts[val]
            prefix.append( (val, total) )
        # Now, perform binary search on the prefix array
        # Find the smallest val such that the cumulative count is >= p
        # We can use bisect_left
        import bisect
        for p in queries:
            low = 0
            high = len(prefix)
            while low < high:
                mid = (low + high) // 2
                if prefix[mid][1] >= p:
                    high = mid
                else:
                    low = mid + 1
            results.append( str(prefix[low][0]) )
    print('\n'.join(results))

if __name__ == '__main__':
    solve()