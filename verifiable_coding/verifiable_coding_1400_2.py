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
        
        # Maximum sum: we need to have unique numbers such that each number is even and half is present
        # Start from 1, then 2, 4, 8, etc. (each number is double the previous)
        # We need to have at least L unique numbers and at most R unique numbers
        # To maximize the sum, we use the maximum possible number of unique elements (R)
        # But we can't have more than R unique elements, so we take R unique elements
        # The maximum sum is the sum of the first R numbers in the sequence 1, 2, 4, 8, ...
        # But we can't have more than N elements, so we take min(R, N) elements
        max_unique = min(R, N)
        max_sum = 0
        current = 1
        for _ in range(max_unique):
            max_sum += current
            current *= 2
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()