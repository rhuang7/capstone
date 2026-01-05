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
            # Time elapsed since last customer
            time_diff = t - (customers[0][0] if customers else 0)
            
            # The temperature can change by at most time_diff
            # So the possible range is [current_temp - time_diff, current_temp + time_diff]
            # We need to find the intersection of this range with [l, h]
            # If there is no intersection, it's impossible
            lower = max(l, current_temp - time_diff)
            upper = min(h, current_temp + time_diff)
            
            if lower > upper:
                possible = False
                break
            
            # Update current temperature to the lower bound of the intersection
            # This is the best way to satisfy the next customer
            current_temp = lower
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()