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
        M = int(data[idx+1])
        S = int(data[idx+2])
        idx += 3
        
        H = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the hours in ascending order to try to take the smallest ones first
        H.sort()
        
        count = 0
        days_used = 0
        
        for h in H:
            # Check if we can take this topic
            if h > S:
                continue  # Cannot take this topic as it exceeds daily limit
            if days_used + 1 > M:
                continue  # Not enough days left
            # Check if we can take this topic in one day
            if h <= S:
                days_used += 1
                count += 1
            else:
                # If h > S, we cannot take it in one day
                continue
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()