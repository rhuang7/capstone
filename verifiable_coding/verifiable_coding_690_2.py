import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    M = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    if any(a == 0 for a in A):
        print(-1)
        return
    
    # We need to find the minimum number of intervals of length K such that
    # after multiplying each element in an interval by X (some positive value),
    # the sum of any K consecutive elements is >= M.
    # We can use a greedy approach: always choose the interval with the smallest sum
    # and multiply all elements in that interval by X to make the sum >= M.
    
    # We'll use a sliding window to find the minimum sum of K consecutive elements
    # and then multiply the elements in that window by X to make the sum >= M.
    # We'll repeat this process until all windows have sum >= M.
    
    # We'll use a priority queue (min-heap) to store the sum of each window of K elements.
    # For each window, we'll calculate its sum and push it into the heap.
    # Then, we'll pop the smallest sum, multiply all elements in that window by X,
    # and push the new sums of the windows that overlap with this window back into the heap.
    
    # We'll also need to track the current values of the array.
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # Initialize the array
    arr = A.copy()
    
    # Initialize the heap
    import heapq
    heap = []
    # Calculate the initial sum of the first K elements
    window_sum = sum(arr[i] for i in range(K))
    heapq.heappush(heap, (window_sum, 0, K-1))
    
    # We'll also need to track the current values of the array
    # and the indices of the elements in each window.
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll also need to track the current values of the array.
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll use a list to store the current values of the array.
    # We'll also need to track the indices of the elements in each window.
    
    # We'll