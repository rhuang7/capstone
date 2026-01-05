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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array
        A.sort()
        
        # The minimum number of operations is determined by the number of elements
        # that are not equal to the median (or any value in the middle of the sorted array)
        # because we can adjust any element to match the median in one operation
        # (since we can add or subtract any odd number, which allows us to reach any value)
        # However, since we can only change one element at a time, the number of operations
        # is equal to the number of elements that are not equal to the median
        median = A[N//2]
        count = 0
        for num in A:
            if num != median:
                count += 1
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()