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
        
        # Create a new array with the required pattern
        result = []
        i = 0
        while i < N:
            # Find the next peak
            peak = arr[i]
            result.append(peak)
            i += 1
            # Find the next valley
            if i < N:
                valley = arr[i]
                result.append(valley)
                i += 1
            # Find the next peak
            if i < N:
                peak = arr[i]
                result.append(peak)
                i += 1
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()