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
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        ages = list(map(int, data[idx:idx+N]))
        idx += N
        
        at_risk = sum(1 for age in ages if age <= 9 or age >= 80)
        non_risk = N - at_risk
        
        days = 0
        # Days needed for at-risk people
        days += (at_risk + D - 1) // D
        # Days needed for non-risk people
        days += (non_risk + D - 1) // D
        
        results.append(days)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()