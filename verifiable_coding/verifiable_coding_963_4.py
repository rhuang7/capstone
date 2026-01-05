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
        h = list(map(int, data[idx:idx+N]))
        idx += N
        
        res = 0
        i = 0
        while i < N:
            res += 1
            # Find the next hill higher than h[i]
            j = i + 1
            while j < N and h[j] <= h[i]:
                j += 1
            i = j
        
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()