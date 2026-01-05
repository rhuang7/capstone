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
        
        unpaid_months = []
        for i in range(N):
            if A[i] == 0:
                unpaid_months.append(i)
        
        total = 0
        for month in unpaid_months:
            total += 1000
            total += 100
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()