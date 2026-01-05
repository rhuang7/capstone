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
        X = list(map(int, data[idx:idx+N]))
        idx += N
        X.sort()
        max_dist = 0
        for i in range(1, N):
            dist = X[i] - X[i-1]
            if dist > max_dist:
                max_dist = dist
        results.append(str(max_dist))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()