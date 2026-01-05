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
        
        unpaid_months = []
        paid_months = []
        
        for i in range(N):
            if A[i] == 1:
                paid_months.append(i)
        
        for i in range(N):
            if A[i] == 0:
                unpaid_months.append(i)
        
        total = 0
        for month in unpaid_months:
            total += 1000
            total += 100
        
        for month in paid_months:
            total += 1000
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()