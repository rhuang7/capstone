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
        
        # Initialize current temperature
        current_temp = m
        
        # Process each customer
        possible = True
        for t, l, h in customers:
            # Time difference
            delta = t - 0  # since current time is 0
            
            # The temperature can be adjusted between [current_temp - delta, current_temp + delta]
            # We need to find a temperature in [l, h] that is within this range
            # The possible range is [current_temp - delta, current_temp + delta]
            # The intersection of [l, h] and [current_temp - delta, current_temp + delta] must be non-empty
            
            # Find the overlap between [l, h] and [current_temp - delta, current_temp + delta]
            lower = max(l, current_temp - delta)
            upper = min(h, current_temp + delta)
            
            if lower > upper:
                possible = False
                break
            
            # Update current temperature to the maximum possible value in the overlap
            # This allows more flexibility for future customers
            current_temp = upper
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()