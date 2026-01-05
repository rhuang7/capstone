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
        
        # Try all possible splits of the top boxes
        for i in range(1, N):
            sum1 = sum(H[:i])
            sum2 = sum(H[i:])
            if sum1 >= K and sum2 >= K:
                min_boxes = min(min_boxes, i + (N - i))
        
        # Check if there's a way to split the top boxes into two parts
        # where one part is at least K and the other part is at least K
        # but not necessarily using all the top boxes
        for i in range(1, N):
            sum1 = sum(H[:i])
            if sum1 >= K:
                # Find the smallest j >= i such that sum(H[i:j]) >= K
                j = i
                while j < N:
                    sum2 = sum(H[i:j])
                    if sum2 >= K:
                        min_boxes = min(min_boxes, j - i + i)
                        break
                    j += 1
        
        results.append(min_boxes if min_boxes != float('inf') else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()