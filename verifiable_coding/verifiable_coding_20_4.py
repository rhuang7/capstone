import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    q = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        customers = []
        for _ in range(n):
            t = int(data[idx])
            l = int(data[idx+1])
            h = int(data[idx+2])
            customers.append((t, l, h))
            idx += 3
        
        # Sort customers by time
        customers.sort()
        
        # Initial temperature
        current_temp = m
        
        # Process each customer
        possible = True
        for t, l, h in customers:
            # Time elapsed since last customer
            time_diff = t - prev_time
            # Update temperature based on time difference
            current_temp += time_diff
            
            # Check if current temperature is within the range
            if not (l <= current_temp <= h):
                possible = False
                break
            
            prev_time = t
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()