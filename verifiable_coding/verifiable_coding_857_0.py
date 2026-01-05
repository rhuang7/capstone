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
        
        dom_times = list(map(int, data[idx:idx+N]))
        idx += N
        
        rival_times = list(map(int, data[idx:idx+N]))
        idx += N
        
        dom_times.sort()
        rival_times.sort()
        
        wins = 0
        for d, r in zip(dom_times, rival_times):
            if d < r:
                wins += 1
        
        results.append(wins)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()