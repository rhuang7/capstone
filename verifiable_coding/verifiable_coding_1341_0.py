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
        
        # Calculate the number of valid contiguous subsequences
        # that when removed leave a strictly increasing sequence
        # We can use a sliding window approach to find increasing runs
        # and compute the number of valid subarrays
        # Initialize variables
        res = 0
        left = 0
        for right in range(N):
            # Maintain a window [left, right] where A[left..right] is increasing
            while left <= right and A[right] <= A[right - 1]:
                left = right
            # The number of valid subarrays ending at right is (right - left + 1)
            res += right - left + 1
        
        # Subtract 1 to exclude the case where the entire array is removed
        res -= 1
        results.append(res)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    solve()