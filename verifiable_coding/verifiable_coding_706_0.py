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
            results.append(-1)
            continue
        
        # Greedy approach: process boxes from right to left
        trips = 0
        current_weight = 0
        # Process from right to left to ensure we can carry boxes in one trip
        for i in range(N-1, -1, -1):
            if current_weight + W[i] > K:
                trips += 1
                current_weight = W[i]
            else:
                current_weight += W[i]
        # Add the last trip
        trips += 1
        results.append(trips)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()