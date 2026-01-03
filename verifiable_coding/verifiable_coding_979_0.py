import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    K = int(data[2])
    
    # For a rectangle to be good, all inner border cells must be the same color
    # The inner border of a rectangle of size m x n is the cells on the edges, excluding the corners
    # The number of inner border cells is 2*(m + n - 2)
    # For a rectangle to be good, all these cells must be the same color
    # The probability that all these cells are the same color is 1/K^(2*(m + n - 2))
    # The total number of rectangles is (M * (M + 1) // 2) * (N * (N + 1) // 2)
    # So the expected number is total_rectangles * probability
    
    total_rectangles = (M * (M + 1) // 2) * (N * (N + 1) // 2)
    
    # For each rectangle, compute the number of inner border cells
    # The expected value is sum over all rectangles of 1/K^(2*(m + n - 2))
    # But since m and n vary, we can compute the sum for all possible m and n
    
    expected = 0
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            border = 2 * (m + n - 2)
            if border > 0:
                prob = 1.0 / (K ** border)
                count = (m * (m + 1) // 2) * (n * (n + 1) // 2)
                expected += count * prob
    
    print(round(expected))

if __name__ == '__main__':
    solve()