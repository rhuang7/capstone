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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # If K is 1, then there is only one flavor, so any subsegment is invalid
        # because there is no other flavor to exclude
        if K == 1:
            results.append(N)
            continue
        
        # We need to find the longest subsegment that does not contain at least one flavor
        # This is equivalent to finding the longest subsegment that is missing at least one flavor
        # So, we can find the maximum length of a subsegment that is missing at least one flavor
        
        # We can use a sliding window approach
        # We will track the count of each flavor in the current window
        # If the number of unique flavors in the window is less than K, then it's a valid subsegment
        
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        max_len = 0
        unique = 0
        
        for right in range(N):
            num = A[right]
            if count[num] == 0:
                unique += 1
            count[num] += 1
            
            # If the number of unique flavors is less than K, it's a valid subsegment
            while unique < K:
                left_num = A[left]
                count[left_num] -= 1
                if count[left_num] == 0:
                    unique -= 1
                left += 1
            
            # Update the maximum length
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        
        results.append(max_len)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()