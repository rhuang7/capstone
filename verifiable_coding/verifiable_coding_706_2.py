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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        W = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if any box weight exceeds K
        if any(w > K for w in W):
            results.append("-1")
            continue
        
        # Greedy approach: process boxes from right to left
        trips = 0
        current_load = 0
        
        for w in reversed(W):
            if current_load + w <= K:
                current_load += w
            else:
                trips += 1
                current_load = w
        
        # Add the last trip
        trips += 1
        results.append(str(trips))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()