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
    # The number of rectangles is (M * (M + 1) // 2) * (N * (N + 1) // 2)
    # For each rectangle, the probability that all inner borders are the same color is 1/K
    # So the expected number is (total_rectangles) * (1/K)

    total_rectangles = (M * (M + 1) // 2) * (N * (N + 1) // 2)
    expected = total_rectangles / K

    # Round to the nearest integer
    print(round(expected))

if __name__ == '__main__':
    solve()