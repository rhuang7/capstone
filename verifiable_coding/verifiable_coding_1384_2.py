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
            # If the current zero is more than K away from the left zero, we need to move left
            if zeros[right] - zeros[left] > K:
                left = right
            # The maximum pizza time is the distance between the current zero and the previous zero plus 1
            # plus the K length of the substring
            current = zeros[right] - zeros[left] + 1 + K
            max_pizza_time = max(max_pizza_time, current)
        
        # Also check the case where we can extend from the end
        if zeros:
            max_pizza_time = max(max_pizza_time, zeros[0] + 1 + K)
        
        results.append(str(max_pizza_time))
    
    print('\n'.join(results)) 

if __name__ == '__main__':
    solve()