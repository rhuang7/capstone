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
        is_sharpened = False
        for k in range(1, n + 1):
            # Check increasing part up to k
            inc = True
            for i in range(1, k):
                if a[i] <= a[i - 1]:
                    inc = False
                    break
            if not inc:
                continue
            
            # Check decreasing part from k
            dec = True
            for i in range(k, n):
                if a[i] <= a[i - 1]:
                    dec = False
                    break
            if dec:
                is_sharpened = True
                break
        
        results.append("Yes" if is_sharpened else "No")
    
    print("\n".join(results))