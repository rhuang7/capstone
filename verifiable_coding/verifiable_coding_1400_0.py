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
        
        # Maximum sum: use the largest possible numbers such that each number is even and half is present
        # We need to find the maximum sum with unique numbers in the range [L, R]
        # The maximum sum is achieved by using the largest possible numbers, starting from 1, 2, 4, 8, ...
        # So we need to find the maximum number of unique elements in [L, R] that can be formed in this way
        # The maximum number of unique elements is min(R, 20) because 2^20 is very large
        # We can generate the sequence 1, 2, 4, 8, ... up to the maximum number of elements allowed
        max_unique = min(R, 20)
        max_elements = []
        current = 1
        for i in range(max_unique):
            max_elements.append(current)
            current *= 2
        # Take the first 'R' elements (if R is less than max_unique)
        max_elements = max_elements[:R]
        # Now, we need to choose exactly 'R' unique elements, but we can choose any subset of size R from the max_elements
        # The maximum sum is achieved by taking the largest R elements
        max_sum = sum(max_elements[-R:])
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()