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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        count = [0] * N
        for num in arr:
            if 0 <= num < N:
                count[num] += 1
        
        result = [0] * N
        for i in range(N):
            if count[i] > 0:
                result[i] = i
                count[i] -= 1
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()