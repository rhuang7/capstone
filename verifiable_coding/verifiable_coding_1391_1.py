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
        from collections import defaultdict
        comparts = defaultdict(list)
        for si, fi, pi in customers:
            comparts[pi].append((si, fi))
        
        # For each compartment, find maximum number of non-overlapping intervals
        # Using greedy algorithm: sort by start time, select earliest ending first
        max_customers = 0
        for comp in comparts.values():
            # Sort by start time
            comp.sort()
            count = 0
            last_end = -1
            for si, fi in comp:
                if si >= last_end:
                    count += 1
                    last_end = fi
            max_customers += count
        
        results.append(str(max_customers))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()