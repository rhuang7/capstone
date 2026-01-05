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
        
        # Check if Hooli will always win
        def will_hooli_win():
            # Calculate days until Hooli reaches Z
            days_hooli = (Z - B + Y - 1) // Y
            if days_hooli < 0:
                return False
            # Calculate days until Pied Piper reaches Z
            days_pied = (Z - A + X - 1) // X
            if days_pied < 0:
                return False
            return days_hooli <= days_pied
        
        if will_hooli_win():
            results.append("RIP")
            continue
        
        # Calculate the minimum contributions needed
        # We need to find the minimum number of contributions to make A + sum(contributions) >= Z
        # Each contribution reduces the contribution value by half
        # We use a priority queue to always take the largest available contribution
        import heapq
        heap = []
        for c in C:
            heapq.heappush(heap, -c)
        
        contributions = 0
        current_a = A
        while True:
            # Check if current_a already reaches Z
            if current_a >= Z:
                break
            # Check if Hooli will reach Z before current_a
            days_pied = (Z - current_a + X - 1) // X
            days_hooli = (Z - B + Y - 1) // Y
            if days_pied >= days_hooli:
                break
            # Take the largest contribution
            if not heap:
                break
            c = -heapq.heappop(heap)
            current_a += c
            contributions += 1
            # Halve the contribution value
            if c > 0:
                heapq.heappush(heap, -c // 2)
        
        results.append(str(contributions))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()