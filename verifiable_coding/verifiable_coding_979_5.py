import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    K = int(data[2])
    
    if K == 1:
        # All cells are the same color, so all rectangles are good
        total_rectangles = M * (M + 1) // 2 * N * (N + 1) // 2
        print(int(total_rectangles))
        return
    
    # For each possible rectangle, the probability that all inner borders are the same color
    # is (1/K)^(number of inner borders)
    # The number of inner borders for a rectangle of size a x b is (a-1) + (b-1)
    # So the probability is (1/K)^(a + b - 2)
    # The total expected value is the sum over all possible rectangles of this probability
    
    # We can iterate over all possible rectangle sizes (a, b)
    # and count how many rectangles of that size exist
    # and multiply by the probability for that size
    
    total = 0
    for a in range(1, M + 1):
        for b in range(1, N + 1):
            # Number of rectangles of size a x b
            count = (M - a + 1) * (N - b + 1)
            # Number of inner borders for this rectangle
            inner_borders = a + b - 2
            # Probability that all inner borders are the same color
            prob = (1 / K) ** inner_borders
            total += count * prob
    
    # Round to the nearest integer
    print(round(total))

if __name__ == '__main__':
    solve()