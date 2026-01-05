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
        
        # The minimum time is the sum of the differences between each element and the median
        # Since we can only add or subtract odd numbers, we need to adjust for parity
        # The median is the best choice to minimize the sum of absolute differences
        
        median = A[N // 2]
        total = 0
        for num in A:
            diff = abs(num - median)
            # To make the difference odd, if it's even, we need to add 1
            if diff % 2 == 0:
                total += diff + 1
            else:
                total += diff
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()