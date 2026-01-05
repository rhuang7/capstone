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
        h = list(map(int, data[idx:idx+N]))
        idx += N
        
        prev = 0
        add = 0
        
        for height in h:
            if height - prev > K:
                add += (height - prev - 1) // K
            prev = height
        
        results.append(str(add))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()