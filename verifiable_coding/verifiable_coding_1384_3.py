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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = data[idx]
        idx += 1
        
        # Preprocess the string to find positions of '0's
        zeros = []
        for i in range(N):
            if A[i] == '0':
                zeros.append(i)
        
        max_pizza_time = 0
        # Sliding window over the zeros
        left = 0
        for right in range(len(zeros)):
            # If the window is larger than K, move left
            if right - left + 1 > K:
                left += 1
            # Check if the current window can be converted to all 1's
            # The window is from zeros[left] to zeros[right]
            # The length of the window is right - left + 1
            # We can convert it to all 1's if the window is <= K
            if right - left + 1 <= K:
                # Calculate the maximum pizza time
                # The converted window spans from zeros[left] to zeros[right]
                # The left part is from start of string to zeros[left]
                # The right part is from zeros[right] to end of string
                # The middle is the converted window
                # The max pizza time is the max of:
                # - start to zeros[left] + (right - left + 1)
                # - zeros[right] to end + (right - left + 1)
                # - the converted window itself
                start = 0
                end = N - 1
                if left > 0:
                    start = zeros[left - 1] + 1
                if right < len(zeros) - 1:
                    end = zeros[right + 1] - 1
                current = end - start + 1
                if current > max_pizza_time:
                    max_pizza_time = current
        
        results.append(str(max_pizza_time))
    
    print('\n'.join(results))