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
        p = int(data[idx])
        q = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        # Check if it's possible to reach the target
        if (a - p) < 0 or (b - q) < 0 or (c - r) < 0:
            results.append("-1")
            continue
        
        # Calculate the differences
        diff_p = a - p
        diff_q = b - q
        diff_r = c - r
        
        # Check if all differences are non-negative
        if diff_p < 0 or diff_q < 0 or diff_r < 0:
            results.append("-1")
            continue
        
        # Count the number of non-zero differences
        count = 0
        if diff_p > 0:
            count += 1
        if diff_q > 0:
            count += 1
        if diff_r > 0:
            count += 1
        
        results.append(str(count))
    
    print("\n".join(results))