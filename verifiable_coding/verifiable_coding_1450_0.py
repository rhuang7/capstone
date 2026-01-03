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
        
        # Create a new array following the pattern arr[i] > arr[i+1] < arr[i+2] > arr[i+3] < ...
        # We can sort the array and place the largest elements in the peaks and valleys
        # Sort the array
        arr.sort()
        
        # Create the result array
        result = []
        # The peak positions are at even indices (0, 2, 4, ...)
        # The valley positions are at odd indices (1, 3, 5, ...)
        # We place the largest elements at the peaks and the next largest at the valleys
        peak_index = 0
        valley_index = 1
        
        for i in range(N):
            if i % 2 == 0:
                # Peak position, take the next largest element
                result.append(arr[peak_index])
                peak_index += 1
            else:
                # Valley position, take the next largest element
                result.append(arr[valley_index])
                valley_index += 1
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()