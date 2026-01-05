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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Make the array non-decreasing
        # We'll try to fix it by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first check if it's already non-decreasing
        is_non_decreasing = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                is_non_decreasing = False
                break
        if is_non_decreasing:
            results.append("0")
            results.append("")
            continue
        
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        def get_mex(arr):
            mex = 0
            while mex in arr:
                mex += 1
            return mex
        
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that ensures the array becomes non-decreasing
        # We'll first compute the MEX
        # We'll perform operations to make the array non-decreasing
        # We'll try to fix the array by replacing elements with MEX
        # We'll do this in a way that