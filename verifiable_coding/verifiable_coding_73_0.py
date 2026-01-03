import sys

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
        # Compute the MEX
        mex = 0
        while mex in arr:
            mex += 1
        
        # Try to fix the array
        operations = []
        for i in range(n):
            if arr[i] > arr[i+1]:
                # Replace the current element with mex
                operations.append(i+1)
                arr[i] = mex
                # Recompute mex
                mex = 0
                while mex in arr:
                    mex += 1
        
        # If not sorted, do more operations
        if arr != sorted(arr):
            for i in range(n):
                if arr[i] > arr[i+1]:
                    operations.append(i+1)
                    arr[i] = mex
                    # Recompute mex
                    mex = 0
                    while mex in arr:
                        mex += 1
        
        results.append(str(len(operations)))
        results.append(' '.join(map(str, operations)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()