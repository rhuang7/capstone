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
            idx += 3
            customers.append((si, fi, pi))
        
        # Group customers by compartment
        comp_rooms = {}
        for si, fi, pi in customers:
            if pi not in comp_rooms:
                comp_rooms[pi] = []
            comp_rooms[pi].append((si, fi))
        
        # For each compartment, select maximum non-overlapping intervals
        # Using greedy algorithm: sort by finish time and select non-overlapping
        max_customers = 0
        for comp in comp_rooms.values():
            # Sort by finish time
            comp.sort(key=lambda x: x[1])
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