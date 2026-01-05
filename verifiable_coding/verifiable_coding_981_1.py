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
        S = list(map(int, data[idx:idx+N]))
        idx += N
        S.sort()
        min_diff = float('inf')
        for i in range(N-1):
            diff = S[i+1] - S[i]
            if diff < min_diff:
                min_diff = diff
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()