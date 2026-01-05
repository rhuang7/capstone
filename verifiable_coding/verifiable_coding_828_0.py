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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Track the number of unpaid months
        unpaid_months = 0
        
        # For each month, if Chef paid, it's used to cover the earliest unpaid month
        for i in range(N):
            if A[i] == 1:
                # This payment is used to cover the earliest unpaid month
                unpaid_months -= 1
                if unpaid_months < 0:
                    unpaid_months = 0
            else:
                # This month is unpaid
                unpaid_months += 1
        
        # Total amount = (unpaid_months * 1000) + (unpaid_months * 100)
        total = unpaid_months * 1000 + unpaid_months * 100
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()