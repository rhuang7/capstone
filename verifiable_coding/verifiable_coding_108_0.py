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
        
        if n == 1:
            results.append("Yes")
            continue
        
        # Find the peak position
        peak = 0
        for i in range(1, n):
            if a[i] > a[i - 1]:
                peak = i
            else:
                break
        
        # Check if the array can be made sharpened
        # Try to make the first part strictly increasing and the second part strictly decreasing
        # We can adjust the elements to ensure this
        
        # Make the first part strictly increasing
        inc = []
        for i in range(n):
            if not inc or a[i] > inc[-1]:
                inc.append(a[i])
            else:
                inc.append(inc[-1] + 1)
        
        # Make the second part strictly decreasing
        dec = []
        for i in range(n - 1, -1, -1):
            if not dec or a[i] > dec[-1]:
                dec.append(a[i])
            else:
                dec.append(dec[-1] - 1)
        
        # Check if there exists a peak such that the first part is increasing and the second part is decreasing
        # We can try all possible peak positions
        found = False
        for k in range(n):
            # Check if the first k elements can be made strictly increasing
            valid_inc = True
            for i in range(1, k + 1):
                if a[i] <= a[i - 1]:
                    valid_inc = False
                    break
            if not valid_inc:
                continue
            
            # Check if the remaining elements can be made strictly decreasing
            valid_dec = True
            for i in range(k + 1, n):
                if a[i] <= a[i - 1]:
                    valid_dec = False
                    break
            if valid_dec:
                found = True
                break
        
        results.append("Yes" if found else "No")
    
    print("\n".join(results))