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
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        customers = []
        for _ in range(N):
            si = int(data[idx])
            fi = int(data[idx+1])
            pi = int(data[idx+2])
            customers.append((si, fi, pi))
            idx += 3
        
        # Group customers by their preferred compartment
        comparts = {}
        for si, fi, pi in customers:
            if pi not in comparts:
                comparts[pi] = []
            comparts[pi].append((si, fi))
        
        # For each compartment, schedule as many customers as possible
        # Using greedy algorithm: sort by start time, then select non-overlapping intervals
        total = 0
        for comp in comparts.values():
            # Sort by start time
            comp.sort()
            count = 0
            last_end = -1
            for si, fi in comp:
                if si >= last_end:
                    count += 1
                    last_end = fi
            total += count
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()