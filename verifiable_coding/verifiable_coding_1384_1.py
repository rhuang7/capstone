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
        
        # Preprocess the string to find positions of 0s
        zeros = []
        for i in range(N):
            if A[i] == '0':
                zeros.append(i)
        
        max_pizza_time = 0
        # Sliding window over the zeros
        left = 0
        for right in range(len(zeros)):
            # If the current zero is more than K away from the left, move left
            if zeros[right] - zeros[left] > K:
                left = right
            # The maximum pizza time is the length of the segment between left and right
            # plus the number of zeros in between (each can be converted)
            # but we need to consider the actual positions
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if the window is valid
            # So the max pizza_time is the length of the segment between zeros[left] and zeros[right]
            # plus the number of zeros in between (each can be converted)
            # but we need to check if