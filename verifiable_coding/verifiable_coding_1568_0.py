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
        idx += 1
        weights = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = sum(weights)
        half = total // 2
        count = 0
        
        for w in weights:
            if w >= half:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()