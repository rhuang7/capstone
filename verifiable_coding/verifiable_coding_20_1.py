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
            # Calculate the time difference
            time_diff = t - 0  # since current time is 0
            
            # Calculate the possible temperature range
            # The temperature can be at most current_temp + time_diff (if heating all the time)
            # The temperature can be at least current_temp - time_diff (if cooling all the time)
            min_temp = current_temp - time_diff
            max_temp = current_temp + time_diff
            
            # Check if there is an overlap between [min_temp, max_temp] and [l, h]
            if h < min_temp or l > max_temp:
                possible = False
                break
            
            # Update current temperature to the maximum possible value that is within the customer's range
            # This is because we want to leave as much flexibility as possible for future customers
            current_temp = min(max_temp, h)
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()