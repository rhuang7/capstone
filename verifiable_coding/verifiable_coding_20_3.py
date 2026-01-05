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
        current_temp = m
        prev_time = 0
        
        possible = True
        for t, l, h in customers:
            if t > prev_time:
                # We can adjust temperature between prev_time and t
                # The temperature can change by (t - prev_time) steps
                # So the possible range is [current_temp - (t - prev_time), current_temp + (t - prev_time)]
                min_temp = current_temp - (t - prev_time)
                max_temp = current_temp + (t - prev_time)
                
                # Find the overlap between [min_temp, max_temp] and [l, h]
                lower = max(l, min_temp)
                upper = min(h, max_temp)
                
                if lower > upper:
                    possible = False
                    break
                # Update current temperature to the lower bound of the overlap
                current_temp = lower
            prev_time = t
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()