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
        total = sum(H)
        if total < 2 * K:
            results.append(-1)
            continue
        
        min_boxes = float('inf')
        for i in range(N):
            if H[i] >= K:
                min_boxes = min(min_boxes, 1 + i + 1)
                break
        if min_boxes == float('inf'):
            results.append(-1)
            continue
        
        for i in range(N):
            for j in range(i + 1, N):
                if H[i] + H[j] >= K:
                    min_boxes = min(min_boxes, 2)
                    break
            if min_boxes == 2:
                break
        
        results.append(min_boxes)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()