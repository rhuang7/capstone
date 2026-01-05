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
        A = int(data[idx+1])
        B = int(data[idx+2])
        X = int(data[idx+3])
        Y = int(data[idx+4])
        Z = int(data[idx+5])
        idx += 6
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if Pied Piper can already take over
        if A >= Z:
            results.append("RIP")
            continue
        if B >= Z:
            results.append("RIP")
            continue
        
        # Function to calculate days to reach Z
        def days_to_reach(target, current, increment):
            if current >= target:
                return 0
            return (target - current + increment - 1) // increment
        
        # Calculate days for each company to reach Z
        days_pied = days_to_reach(Z, A, X)
        days_hooli = days_to_reach(Z, B, Y)
        
        # If Hooli reaches first or same day, output RIP
        if days_hooli <= days_pied:
            results.append("RIP")
            continue
        
        # Now, find the minimum contributions needed
        # We need to find the minimum number of contributions to make A + sum of contributions >= Z
        # But we can only contribute until the day Hooli reaches Z
        
        # Calculate how many days we have to contribute
        max_days = days_pied - 1
        
        # Use a priority queue to greedily take the largest contributions
        from heapq import heappush, heappop
        
        # Create a max heap (using negative values)
        heap = []
        for c in C:
            while c > 0:
                heappush(heap, -c)
                c = c // 2
        
        contributions = 0
        total_users = A
        days = 0
        
        while days < max_days and heap:
            # Take the largest contribution
            val = -heappop(heap)
            total_users += val
            contributions += 1
            # Check if we have reached or surpassed Z
            if total_users >= Z:
                break
            days += 1
        
        # Check if we have reached Z before the day Hooli reaches
        if total_users >= Z:
            results.append(str(contributions))
        else:
            results.append("RIP")
    
    for res in results:
        print(res)