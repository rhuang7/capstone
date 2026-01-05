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
        
        # If K is 1, then no subsegment can have all K flavors, so the answer is N
        if K == 1:
            results.append(N)
            continue
        
        # Use a sliding window approach to find the longest subarray that does not contain all K flavors
        # We'll track the count of each flavor in the current window
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        max_len = 0
        unique = 0
        
        for right in range(N):
            flavor = A[right]
            if count[flavor] == 0:
                unique += 1
            count[flavor] += 1
            
            # If the window contains all K flavors, move left pointer
            while unique == K:
                left_flavor = A[left]
                count[left_flavor] -= 1
                if count[left_flavor] == 0:
                    unique -= 1
                left += 1
            
            # Update the maximum length of the valid subarray
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        
        results.append(max_len)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()