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
            # Check if there are at least K zeros starting from i
            if i + K <= len(zeros):
                # The window starts at zeros[i] and ends at zeros[i + K - 1]
                start = zeros[i]
                end = zeros[i + K - 1]
                
                # Find the maximum consecutive 1s around this window
                # Check left side
                left = start
                while left >= 0 and A[left] == '1':
                    left -= 1
                left += 1
                
                # Check right side
                right = end
                while right < N and A[right] == '1':
                    right += 1
                right -= 1
                
                # The maximum pizza time is right - left + 1
                max_pizza_time = max(max_pizza_time, right - left + 1)
        
        results.append(str(max_pizza_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()