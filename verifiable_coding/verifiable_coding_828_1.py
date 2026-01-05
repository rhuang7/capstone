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
        
        # Track the number of times a payment was made for a previous month
        payment_for_previous = 0
        
        for i in range(N):
            if A[i] == 1:
                payment_for_previous += 1
            else:
                unpaid_months += 1
        
        # Each unpaid month contributes 1000 + 100 = 1100
        total = unpaid_months * 1100
        
        # Each payment made for a previous month contributes 100 fine
        total += payment_for_previous * 100
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()