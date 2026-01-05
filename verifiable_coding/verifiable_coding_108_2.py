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
        
        if n == 1:
            results.append("Yes")
            continue
        
        # Find the peak position
        peak = 0
        for i in range(1, n):
            if a[i] > a[i-1]:
                peak = i
            else:
                break
        
        # Check if the array can be made sharpened
        # Try to make the first part strictly increasing and the second part strictly decreasing
        # We need to ensure that the peak is the maximum in the array
        # We can decrease elements to make this possible
        
        # Make the first part strictly increasing
        for i in range(1, peak + 1):
            if a[i] <= a[i-1]:
                a[i] = a[i-1] - 1
        
        # Make the second part strictly decreasing
        for i in range(peak, n):
            if a[i] >= a[i+1]:
                a[i] = a[i+1] - 1
        
        # Check if the array is sharpened
        is_sharpened = True
        for i in range(1, peak + 1):
            if a[i] <= a[i-1]:
                is_sharpened = False
                break
        if is_sharpened:
            for i in range(peak, n-1):
                if a[i] <= a[i+1]:
                    is_sharpened = False
                    break
        results.append("Yes" if is_sharpened else "No")
    
    print("\n".join(results))