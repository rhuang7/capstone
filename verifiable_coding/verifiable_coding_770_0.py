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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # We can take at most one even number in any window of size k+1
        # Similarly for odd numbers
        # We will track the maximum sum for even and odd numbers separately
        
        # For even numbers
        even = []
        for num in a:
            if num % 2 == 0:
                even.append(num)
        
        # For odd numbers
        odd = []
        for num in a:
            if num % 2 == 1:
                odd.append(num)
        
        # We can take at most one even number in any window of size k+1
        # So we can take the maximum even number in each window of size k+1
        # Similarly for odd numbers
        
        # Function to find maximum sum by taking at most one element in each window of size k+1
        def max_sum(arr, k):
            max_sum = 0
            i = 0
            while i < len(arr):
                # Take the maximum in the current window
                window_max = max(arr[i:i+k+1])
                max_sum += window_max
                i += k + 1
            return max_sum
        
        # Calculate max sum for even and odd
        max_even = max_sum(even, k)
        max_odd = max_sum(odd, k)
        
        # The answer is the sum of the maximum even and maximum odd
        results.append(str(max_even + max_odd))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()