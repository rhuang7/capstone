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
            # Find the next peak element
            peak = arr[i]
            # Find the next valley element
            valley = arr[i+1] if i+1 < N else peak
            # Find the next peak element after valley
            next_peak = arr[i+2] if i+2 < N else peak
            # Arrange in the pattern peak, valley, peak
            result.append(peak)
            result.append(valley)
            result.append(next_peak)
            i += 3
        
        # If the array length is not a multiple of 3, adjust the last elements
        if len(result) > N:
            result = result[:N]
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()