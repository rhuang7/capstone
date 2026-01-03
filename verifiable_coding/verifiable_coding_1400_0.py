import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        L = int(data[index+1])
        R = int(data[index+2])
        index += 3
        
        # Minimum sum
        min_sum = 0
        # We need at least L unique numbers, and at most R unique numbers
        # For minimum sum, use as many 1s as possible and then the smallest possible even numbers
        # The unique numbers must be 1, 2, 4, 8, ..., 2^k
        # So the minimum sum is when we have L unique numbers, each as small as possible
        # The first L unique numbers are 1, 2, 4, 8, ..., 2^(L-1)
        # The sum of these is 2^L - 1
        # Then the remaining N - L elements are 1s
        min_sum = (2 ** L) - 1
        min_sum += (N - L) * 1
        
        # Maximum sum
        # For maximum sum, use as many as possible of the largest possible numbers
        # The maximum number of unique numbers is R
        # The unique numbers are 1, 2, 4, 8, ..., 2^(R-1)
        # The sum of these is 2^R - 1
        # Then the remaining N - R elements are the largest possible number (2^(R-1))
        max_sum = (2 ** R) - 1
        max_sum += (N - R) * (2 ** (R - 1))
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()