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
        H = list(map(int, data[idx:idx+N]))
        idx += N
        
        H.sort(reverse=True)
        min_boxes = float('inf')
        
        # Check if it's possible to build two towers
        if sum(H) < 2 * K:
            results.append(-1)
            continue
        
        # Try all possible splits of the sorted list
        for i in range(1, N):
            # First tower is first i boxes, second tower is remaining
            if sum(H[:i]) >= K and sum(H[i:]) >= K:
                min_boxes = min(min_boxes, i + (N - i))
                break
        
        # Try all possible combinations of boxes
        for i in range(1, N):
            for j in range(i+1, N+1):
                if sum(H[:i]) >= K and sum(H[i:j]) >= K:
                    min_boxes = min(min_boxes, i + (j - i))
                    break
            if min_boxes != float('inf'):
                break
        
        results.append(min_boxes if min_boxes != float('inf') else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()