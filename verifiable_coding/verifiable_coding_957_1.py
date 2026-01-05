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
        max_distance = 0
        for i in range(1, N):
            distance = X[i] - X[i-1]
            if distance > max_distance:
                max_distance = distance
        results.append(str(max_distance))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()