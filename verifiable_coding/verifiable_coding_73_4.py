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
        # We'll track the current MEX
        mex = 0
        while mex in arr:
            mex += 1
        
        # We'll try to make the array non-decreasing by fixing elements
        # First, check if it's already non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_non_decreasing = False
                break
        
        if is_non_decreasing:
            results.append("0")
            results.append("")
            continue
        
        # If not, we need to perform operations
        # We'll use a list to track the operations
        ops = []
        
        # First, try to fix elements one by one
        for i in range(n):
            if arr[i] > arr[i+1]:
                # Replace arr[i] with mex
                arr[i] = mex
                ops.append(i+1)
                # Recompute mex
                mex = 0
                while mex in arr:
                    mex += 1
        
        # If after this it's not non-decreasing, we need to do more operations
        # We'll do up to 2n operations
        for i in range(n):
            if arr[i] > arr[i+1]:
                # Replace arr[i] with mex
                arr[i] = mex
                ops.append(i+1)
                # Recompute mex
                mex = 0
                while mex in arr:
                    mex += 1
        
        # Now, check if it's non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_non_decreasing = False
                break
        
        # If not, we need to do more operations (but according to problem statement, it's always possible)
        # We'll do up to 2n operations
        for i in range(n):
            if arr[i] > arr[i+1]:
                # Replace arr[i] with mex
                arr[i] = mex
                ops.append(i+1)
                # Recompute mex
                mex = 0
                while mex in arr:
                    mex += 1
        
        # Now, output the result
        results.append(str(len(ops)))
        results.append(' '.join(map(str, ops)))
    
    print('\n'.join(results))