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
        
        # Calculate the day when each company reaches Z users
        def get_day(current, daily):
            if current >= Z:
                return 0
            return (Z - current + daily - 1) // daily
        
        day_pied = get_day(A, X)
        day_hooli = get_day(B, Y)
        
        if day_hooli <= day_pied:
            results.append("RIP")
            continue
        
        # Now find the minimum number of contributions needed
        # To reach or surpass Z users by day_pied
        # We need to find the minimum contributions to get A + sum(contributions) >= Z
        # But we have to consider that contributions are done before the day_pied
        
        # Calculate how many users Pied needs
        needed = Z - A
        
        # Use a max heap to select the best contributors
        import heapq
        heapq.heapify(C)
        # Reverse the heap to get max heap behavior
        C = [-x for x in C]
        heapq.heapify(C)
        
        contributions = 0
        while needed > 0:
            if not C:
                results.append("RIP")
                break
            val = -heapq.heappop(C)
            if val >= needed:
                contributions += 1
                needed = 0
            else:
                contributions += 1
                needed -= val
                # Halve the value
                val = val // 2
                heapq.heappush(C, -val)
        else:
            results.append(str(contributions))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()