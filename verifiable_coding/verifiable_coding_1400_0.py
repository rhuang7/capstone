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
        L = int(data[idx+1])
        R = int(data[idx+2])
        idx += 3
        
        # Minimum sum: all elements are 1
        min_sum = N * 1
        
        # Maximum sum: use the largest possible unique numbers such that each number is even and half is present
        # We need to find the maximum number of unique elements between L and R
        # The maximum possible unique elements is min(R, N)
        max_unique = min(R, N)
        # Start from 1 and double each time (1, 2, 4, 8, 16, ...)
        # We need max_unique elements
        max_sum = 0
        current = 1
        for _ in range(max_unique):
            max_sum += current
            current *= 2
        results.append(f"{min_sum} {max_sum}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()