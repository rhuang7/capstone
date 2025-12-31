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
        
        # If no unpaid month, then no fines
        if first_unpaid == -1:
            results.append(0)
            continue
        
        # For each month, check if it was used to pay an unpaid month
        # The first unpaid month is the one that will be paid by the first 1
        # All 1s after that will be used to pay for the unpaid months after first_unpaid
        # Each unpaid month (including first_unpaid) will have a fine of 100
        # Each unpaid month will have a maintenance fee of 1000
        # So total for each unpaid month is 1100
        # But the first unpaid month is paid by the first 1, so no fine
        # All other unpaid months will have a fine
        
        # Count the number of unpaid months
        unpaid_count = 0
        for i in range(N):
            if A[i] == 0:
                unpaid_count += 1
        
        # The first unpaid month is paid by the first 1
        # So the first unpaid month has no fine
        # The rest of the unpaid months have a fine
        fines = (unpaid_count - 1) * 100
        
        # Total amount is (unpaid_count * 1000) + (fines)
        total = unpaid_count * 1000 + fines
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()