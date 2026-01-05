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
        scores = list(map(int, data[idx:idx+N]))
        idx += N
        
        scores.sort(reverse=True)
        cutoff = scores[K-1]
        count = 0
        for s in scores:
            if s >= cutoff:
                count += 1
            else:
                break
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()