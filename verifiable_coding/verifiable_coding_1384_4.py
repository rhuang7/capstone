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
        # Slide a window of size K over the zeros
        for i in range(len(zeros) - K + 1):
            # The window starts at zeros[i], ends at zeros[i+K-1]
            start = zeros[i]
            end = zeros[i+K-1]
            
            # Check the maximum consecutive 1s that can be formed by flipping K 0s
            # The flipped 0s are from start to end
            # We need to check the maximum sequence of 1s that can be formed by including this window
            # Check the left side of the window
            left = start
            while left >= 0 and A[left] == '1':
                left -= 1
            left += 1
            
            # Check the right side of the window
            right = end
            while right < N and A[right] == '1':
                right += 1
            right -= 1
            
            # The maximum pizza time is right - left + 1
            current = right - left + 1
            if current > max_pizza_time:
                max_pizza_time = current
        
        results.append(str(max_pizza_time))
    
    print('\n'.join(results))