import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        A = list(map(int, data[index:index + N]))
        index += N
        
        unpaid = 0
        fines = 0
        
        # Find the first month where Chef did not pay
        first_unpaid = -1
        for i in range(N):
            if A[i] == 0:
                first_unpaid = i
                break
        
        # If no unpaid months, then no fines
        if first_unpaid == -1:
            results.append(0)
            continue
        
        # Count the number of months where Chef paid after the first unpaid month
        paid_after = 0
        for i in range(N):
            if A[i] == 1:
                paid_after += 1
        
        # Each unpaid month incurs a fine of 100
        fines = (N - paid_after) * 100
        
        # Each unpaid month also incurs a maintenance fee of 1000
        unpaid = (N - paid_after) * 1000
        
        total = unpaid + fines
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()