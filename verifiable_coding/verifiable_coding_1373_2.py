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
        
        # If K is 1, then all elements are the same, so the entire array is invalid
        if K == 1:
            results.append(N)
            continue
        
        # Use a sliding window approach to find the maximum subarray
        # that does not contain at least one of the K flavors
        # We'll track the last occurrence of each flavor
        last_occurrence = {}
        max_len = 0
        left = 0
        
        for right in range(N):
            flavor = A[right]
            if flavor in last_occurrence:
                left = max(left, last_occurrence[flavor] + 1)
            last_occurrence[flavor] = right
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        
        # The maximum valid subsegment is the entire array minus the minimal occurrence of any flavor
        # But since we're looking for a subsegment that excludes at least one flavor, the answer is N - min_occurrence
        # However, the sliding window approach already gives the maximum length of a subsegment that contains all K flavors
        # So the answer is N - min_occurrence
        # But since we are looking for a subsegment that excludes at least one flavor, the answer is the maximum length of a subsegment that does not contain at least one flavor
        # Which is the entire array minus the minimal occurrence of any flavor
        # So we need to find the minimal occurrence of any flavor in the array
        # Then the answer is N - min_occurrence
        
        # Count occurrences of each flavor
        from collections import defaultdict
        count = defaultdict(int)
        for flavor in A:
            count[flavor] += 1
        min_occurrence = min(count.values())
        results.append(N - min_occurrence)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()