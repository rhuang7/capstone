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
        
        # Function to calculate days to reach Z
        def get_days(current, daily):
            if current >= Z:
                return 0
            return (Z - current + daily - 1) // daily
        
        # Check if Hooli will always win
        days_pied = get_days(A, X)
        days_hooli = get_days(B, Y)
        if days_hooli <= days_pied:
            results.append("RIP")
            continue
        
        # Now find the minimum contributions
        # Use a max heap to get the largest contributions first
        import heapq
        heapq.heapify(C)
        # Reverse the heap to get max heap behavior
        C = [-x for x in C]
        heapq.heapify(C)
        
        contributions = 0
        current_a = A
        current_b = B
        
        while True:
            # Check if current_a and current_b have reached or surpassed Z
            if current_a >= Z:
                break
            if current_b >= Z:
                results.append("RIP")
                break
            
            # Get the best contribution
            best = -heapq.heappop(C)
            # Add the contribution
            current_a += best
            contributions += 1
            # Halve the contribution
            best = best // 2
            # Push back the halved value
            heapq.heappush(C, -best)
        
        results.append(str(contributions))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()