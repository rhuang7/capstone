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
        A = list(map(int, data[idx:idx+5]))
        P = int(data[idx+5])
        idx += 6
        
        total_work = sum(a * P for a in A)
        max_work_per_day = 24
        
        if total_work > 5 * max_work_per_day:
            results.append("Yes")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()