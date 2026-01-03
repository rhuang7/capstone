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
        
        # Check each customer
        possible = True
        for t, l, h in customers:
            # Time difference
            delta = t - 0  # current time is 0
            # The temperature can vary between current_temp - delta and current_temp + delta
            # Because we can heat or cool for delta minutes
            min_temp = current_temp - delta
            max_temp = current_temp + delta
            
            # Check if the customer's preferred range overlaps with [min_temp, max_temp]
            if h < min_temp or l > max_temp:
                possible = False
                break
            
            # Update current temperature to the maximum possible value within the customer's range
            # This allows for more flexibility in the future
            current_temp = min(max_temp, h)
        
        results.append("YES" if possible else "NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()