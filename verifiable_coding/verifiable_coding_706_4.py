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
        
        # Check if any box is heavier than K
        if any(w > K for w in W):
            results.append(-1)
            continue
        
        # Sort boxes in descending order to try to carry heavier ones first
        W.sort(reverse=True)
        trips = 0
        i = 0
        
        while i < N:
            # Try to carry as many boxes as possible in one trip
            total = 0
            j = i
            while j < N and total + W[j] <= K:
                total += W[j]
                j += 1
            trips += 1
            i = j
        
        results.append(trips)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()