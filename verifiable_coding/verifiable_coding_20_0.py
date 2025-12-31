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
        prev_time = 0
        
        possible = True
        
        for t, l, h in customers:
            # Time elapsed since last customer
            time_diff = t - prev_time
            
            # The temperature can change by at most time_diff
            # So the new temperature can be in [current_temp - time_diff, current_temp + time_diff]
            # We need to find a temperature in this range that is within [l, h]
            
            # The minimum possible temperature is max(current_temp - time_diff, l)
            # The maximum possible temperature is min(current_temp + time_diff, h)
            
            # If there is no overlap, it's impossible
            if current_temp - time_diff > h or current_temp + time_diff < l:
                possible = False
                break
            
            # Update current temperature to the maximum possible value within the range
            # This allows more flexibility for future customers
            current_temp = min(current_temp + time_diff, h)
            prev_time = t
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()