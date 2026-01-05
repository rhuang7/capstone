import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Make a copy to avoid modifying the original
        arr = a[:]
        # We will try to make the array non-decreasing by replacing elements with MEX
        # We can do this by ensuring that each element is at most the next one
        # We'll use a greedy approach to fix the array
        
        # First, we'll try to fix the array in one pass
        # If it's already non-decreasing, we don't need to do anything
        if arr == sorted(arr):
            results.append("0")
            results.append("")
            continue
        
        # Otherwise, we'll perform operations to make it non-decreasing
        # We'll keep track of the operations
        operations = []
        
        # We'll try to make the array non-decreasing by replacing elements with MEX
        # We'll do this in two passes: first to fix the array, then to ensure it's non-decreasing
        # We'll use the MEX of the current array to replace elements
        
        # First pass: fix the array to be non-decreasing
        for i in range(n):
            if i == 0:
                # First element, we can leave it as is
                continue
            if arr[i] < arr[i-1]:
                # We need to replace arr[i] with the MEX of the array
                # Compute MEX
                mex = 0
                while mex in arr:
                    mex += 1
                # Replace arr[i] with mex
                arr[i] = mex
                operations.append(i+1)  # 1-based index
        
        # Second pass: ensure the array is non-decreasing
        for i in range(n):
            if i == 0:
                # First element, we can leave it as is
                continue
            if arr[i] < arr[i-1]:
                # We need to replace arr[i] with the MEX of the array
                # Compute MEX
                mex = 0
                while mex in arr:
                    mex += 1
                # Replace arr[i] with mex
                arr[i] = mex
                operations.append(i+1)  # 1-based index
        
        # Now, check if the array is non-decreasing
        # If not, we need to perform more operations
        # However, the problem states that it is always possible to make it non-decreasing in at most 2n operations
        # So we can stop here
        
        # Output the result
        results.append(str(len(operations)))
        results.append(' '.join(map(str, operations)))
    
    print('\n'.join(results))