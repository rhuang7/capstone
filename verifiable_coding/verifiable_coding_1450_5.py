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
        for i in range(0, N, 3):
            if i + 2 < N:
                result.append(arr[i + 1])
                result.append(arr[i])
                result.append(arr[i + 2])
            else:
                # Handle the case when there are less than 3 elements left
                if i + 1 < N:
                    result.append(arr[i + 1])
                    result.append(arr[i])
                else:
                    result.append(arr[i])
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()