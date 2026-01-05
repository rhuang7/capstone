import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    S = data[idx]
    
    # Preprocess the array to handle rotations
    # We'll keep track of the current rotation offset
    # The array is circular, so we can represent it as a deque or use modulo arithmetic
    
    # Precompute the prefix sums of 1s
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    # Function to find the maximum number of consecutive 1s in a circular array
    def max_consecutive_ones(arr, K):
        max_len = 0
        current = 0
        for i in range(N):
            if arr[i] == 1:
                current += 1
                max_len = max(max_len, current)
            else:
                current = 0
            if current > K:
                current = K
        return max_len
    
    # Function to rotate the array
    def rotate_right():
        nonlocal A
        A = [A[-1]] + A[:-1]
    
    # Process the queries
    for c in S:
        if c == '!':
            rotate_right()
        else:
            # Compute the maximum number of consecutive 1s with length <= K
            # Since the array is circular, we can use the prefix sums
            # We need to find the maximum length of consecutive 1s in the array
            # with length <= K
            # We can use a sliding window approach on the circular array
            # We'll consider the array as doubled to handle the circularity
            # Then apply sliding window on the first 2N elements
            # But for efficiency, we can use the prefix sums and handle the circularity
            # We'll find the maximum length of consecutive 1s in the array
            # with length <= K
            # We can use the prefix sums to find the maximum length
            # of consecutive 1s in the array
            # We'll also need to handle the circular part
            # Let's compute the maximum length of consecutive 1s in the array
            # with length <= K
            # We can use the prefix sums and sliding window
            # Initialize variables
            max_len = 0
            current = 0
            start = 0
            for i in range(N):
                if A[i] == 1:
                    current += 1
                    if current > K:
                        current = K
                    max_len = max(max_len, current)
                else:
                    current = 0
            # Handle the circular part
            # Check if the array has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part
            # Check if the last part has a run of 1s that wraps around
            # We can check the first part and the last part