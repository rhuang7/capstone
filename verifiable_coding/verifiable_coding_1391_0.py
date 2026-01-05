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
        
        # Group customers by their preferred compartment
        from collections import defaultdict
        comp_rooms = defaultdict(list)
        for si, fi, pi in customers:
            comp_rooms[pi].append((si, fi))
        
        # For each compartment, find the maximum number of non-overlapping intervals
        # This is the classic interval scheduling problem
        # Sort by start time and greedily select non-overlapping intervals
        max_customers = 0
        for room in comp_rooms.values():
            # Sort by start time
            room.sort()
            count = 0
            last_end = -1
            for si, fi in room:
                if si >= last_end:
                    count += 1
                    last_end = fi
            max_customers += count
        
        results.append(str(max_customers))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()