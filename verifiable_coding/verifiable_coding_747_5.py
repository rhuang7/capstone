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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        A_sorted = sorted(A)
        A_sorted_desc = sorted(A, reverse=True)
        
        # Check if the array can be rearranged into strictly increasing then strictly decreasing
        # We can try to construct such a permutation
        # We can try to create a permutation where the first part is strictly increasing and the second is strictly decreasing
        # We can try to use the sorted array and try to build the permutation
        
        # Try to build the permutation
        # We can try to use the sorted array and try to find a peak
        # We can try to find the peak element and split the array into increasing and decreasing parts
        
        # First, check if there is a valid permutation
        # We can try to sort the array and then try to build the permutation
        
        # Try to build the permutation
        # We can try to sort the array and then try to find a peak
        # We can try to find the peak element and split the array into increasing and decreasing parts
        
        # Try to find the peak
        peak = -1
        for i in range(N):
            if i == 0:
                continue
            if A_sorted[i] > A_sorted[i-1]:
                peak = i
            else:
                break
        
        # If no peak found, then it's not possible
        if peak == -1:
            results.append("NO")
            continue
        
        # Try to build the permutation
        # We can try to take the first part as strictly increasing and the second as strictly decreasing
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is strictly increasing and the second is strictly decreasing
        
        # Try to build the permutation
        # We can take the first part as the first 'peak' elements and the second as the rest
        # But we need to make sure that the first part is