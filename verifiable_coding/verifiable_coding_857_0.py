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
        
        # Sort both lists
        dom_times.sort()
        rival_times.sort()
        
        # Greedily match the fastest dom racer against the fastest rival racer
        # to maximize the number of wins
        dom_ptr = 0
        rival_ptr = 0
        wins = 0
        
        while dom_ptr < N and rival_ptr < N:
            if dom_times[dom_ptr] < rival_times[rival_ptr]:
                wins += 1
            dom_ptr += 1
            rival_ptr += 1
        
        results.append(wins)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()