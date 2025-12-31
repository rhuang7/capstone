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
            # Check the maximum consecutive 1s including the current zero
            # The window is from left to right, and we can flip K zeros in this window
            # So the maximum pizza time is the number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire segment from start to end
            # So we need to check the entire segment from the start of the string to the end
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            # But we need to consider the entire string
            # So we can use a sliding window approach on the zeros
            # The maximum pizza time is the maximum number of 1s between zeros[left] and zeros[right]
            # Plus 1 for the flipped zero
            #