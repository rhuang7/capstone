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
        # Try each window of K consecutive 0s
        for i in range(len(zeros)):
            # Check if there are enough 0s to cover a window of size K
            if i + K - 1 < len(zeros):
                # The window starts at zeros[i], ends at zeros[i + K - 1]
                # The length of the consecutive 1s between these 0s
                # is (zeros[i] - prev_zero - 1) + (next_zero - zeros[i + K - 1] - 1) + K
                # But we need to handle edge cases
                start = zeros[i]
                end = zeros[i + K - 1]
                
                # Left part
                left = start
                if i > 0:
                    left = zeros[i - 1] + 1
                # Right part
                right = end
                if i + K - 1 < len(zeros) - 1:
                    right = zeros[i + K] - 1
                
                # The length of the consecutive 1s after converting K 0s to 1s
                current = (right - left + 1)
                if current > max_pizza_time:
                    max_pizza_time = current
        
        # Also consider the case where all 0s are converted to 1s
        # The maximum pizza time is the length of the entire string
        # if all 0s are converted to 1s
        # But we already considered that in the loop
        results.append(str(max_pizza_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()