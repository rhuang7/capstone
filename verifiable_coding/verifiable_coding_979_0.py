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
    # We calculate the expected number by summing over all possible rectangles

    # Total number of rectangles is (M*(M+1)//2) * (N*(N+1)//2)
    total_rectangles = M * (M + 1) // 2 * N * (N + 1) // 2

    # For each rectangle, the number of inner borders is (width - 1) * (height - 1)
    # So the expected contribution is total_rectangles * (1/K)^(number of inner borders)
    # But since the number of inner borders varies, we need to sum over all possible rectangles

    # We can precompute the sum of (1/K)^(width-1)*(height-1) for all possible widths and heights
    # Let's compute the sum for all possible widths and heights

    sum_expected = 0
    for width in range(1, N + 1):
        for height in range(1, M + 1):
            inner_borders = (width - 1) * (height - 1)
            prob = (1 / K) ** inner_borders
            sum_expected += prob

    expected = total_rectangles * sum_expected
    print(round(expected))

if __name__ == '__main__':
    solve()