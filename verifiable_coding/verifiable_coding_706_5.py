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
        
        # Sort the boxes in descending order of weight
        W.sort(reverse=True)
        
        trips = 0
        i = 0
        while i < N:
            total = 0
            # Try to carry as many boxes as possible in one trip
            while i < N and total + W[i] <= K:
                total += W[i]
                i += 1
            trips += 1
        
        results.append(trips)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()