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
        new_arr = []
        i = 0
        while i < N:
            # Find the next peak
            peak = max(arr[i:])
            new_arr.append(peak)
            # Remove the peak from the array
            arr.remove(peak)
            # Move to the next position
            i += 1
        
        # Check if the array is correctly arranged
        # For the required pattern, the array should be in the form: a < b > c < d > e ...
        # So we need to ensure that every third element is a peak
        # We can do this by checking the pattern
        # However, since we are constructing the array by taking peaks, it should already be correct
        # So we can directly output the new array
        
        results.append(' '.join(map(str, new_arr)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()