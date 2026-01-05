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
        # We'll track the operations
        ops = []
        
        # First, check if the array is already non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_non_decreasing = False
                break
        if is_non_decreasing:
            results.append("0")
            results.append("")
            continue
        
        # Try to fix the array by making it non-decreasing
        # We'll use the MEX approach
        for i in range(n):
            # Compute MEX
            mex = 0
            while mex in arr:
                mex += 1
            # Replace the i-th element with mex
            arr[i] = mex
            ops.append(i+1)  # 1-based index
        
        # Now check if the array is non-decreasing
        is_non_decreasing = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                is_non_decreasing = False
                break
        if is_non_decreasing:
            results.append(str(len(ops)))
            results.append(' '.join(map(str, ops)))
            continue
        
        # If not, perform additional operations
        # We'll perform up to 2n operations
        for i in range(n):
            # Compute MEX
            mex = 0
            while mex in arr:
                mex += 1
            # Replace the i-th element with mex
            arr[i] = mex
            ops.append(i+1)
            if len(ops) >= 2*n:
                break
        
        results.append(str(len(ops)))
        results.append(' '.join(map(str, ops)))
    
    print('\n'.join(results))