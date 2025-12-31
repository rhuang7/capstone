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
    
    # For each possible rectangle, calculate the probability that all inner borders are the same color
    # The number of rectangles of size i x j is (M - i + 1) * (N - j + 1)
    # The probability that all inner borders are the same color is (1/K)^(number of inner borders)
    # The number of inner borders for a rectangle of size i x j is 2*(i-1) + 2*(j-1) = 2*(i + j - 2)
    # So the probability is (1/K)^(2*(i + j - 2))
    
    total = 0
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            borders = 2 * (i + j - 2)
            if borders > 0:
                prob = (1.0 / K) ** borders
            else:
                prob = 1.0
            count = (M - i + 1) * (N - j + 1)
            total += count * prob
    
    # Round to the nearest integer
    print(round(total))

if __name__ == '__main__':
    solve()