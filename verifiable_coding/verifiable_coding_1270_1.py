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
        
        # Try all possible ways to split the boxes into two towers
        for i in range(1, N):
            # First tower is first i boxes
            # Second tower is remaining boxes
            sum1 = sum(H[:i])
            sum2 = sum(H[i:])
            if sum1 >= K and sum2 >= K:
                min_boxes = min(min_boxes, i + (N - i))
        
        # Try all possible ways to split the boxes into two towers with one box in each
        # Check if there are two boxes with sum >= K
        for i in range(N):
            for j in range(i+1, N):
                if H[i] + H[j] >= K:
                    min_boxes = min(min_boxes, 2)
        
        results.append(min_boxes if min_boxes != float('inf') else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()