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
        
        # Calculate days until each company reaches Z
        def days_to_reach(target, current, gain_per_day):
            if current >= target:
                return 0
            return (target - current + gain_per_day - 1) // gain_per_day
        
        days_pied = days_to_reach(Z, A, X)
        days_hooli = days_to_reach(Z, B, Y)
        
        if days_hooli <= days_pied:
            results.append("RIP")
            continue
        
        # Now find the minimum contributions needed
        # Use a max heap to always take the largest contribution
        import heapq
        heapq.heapify(C)
        # Reverse the heap to make it a max heap
        C = [-x for x in C]
        heapq.heapify(C)
        
        contributions = 0
        current_pied = A
        current_hooli = B
        
        while True:
            # Check if we have already reached the goal
            if current_pied >= Z:
                break
            if current_hooli >= Z:
                results.append("RIP")
                break
            
            # Take the largest contribution
            val = -heapq.heappop(C)
            contributions += 1
            current_pied += val
            val //= 2
            # Put back the halved value
            heapq.heappush(C, -val)
        
        results.append(str(contributions))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()