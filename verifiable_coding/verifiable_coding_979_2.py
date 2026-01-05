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
    
    # For each possible rectangle, calculate the probability that its inner border is the same color
    # The inner border of a rectangle of size h x w (height h, width w) has (h-2)*w + (w-2)*h = 2hw - 4h - 4w + 4
    # But for a rectangle with height 1 or width 1, there is no inner border
    # So we only consider rectangles with height >= 2 and width >= 2
    
    total = 0
    for h in range(2, M + 1):
        for w in range(2, N + 1):
            # Number of rectangles of size h x w
            count = (M - h + 1) * (N - w + 1)
            # Probability that the inner border is the same color
            # There are (h-2)*w + (w-2)*h = 2hw - 4h - 4w + 4 cells in the inner border
            # Each cell has probability 1/K to be the same color as the first cell
            # So the probability is (1/K)^(2hw - 4h - 4w + 4)
            # But since the inner border is a single color, we have to choose that color
            # So the probability is (1/K)^(number of inner border cells)
            # But since the color is chosen uniformly, the probability is (1/K)^(number of inner border cells)
            inner_border_cells = 2 * h * w - 4 * h - 4 * w + 4
            prob = (1.0 / K) ** inner_border_cells
            total += count * prob
    
    # Round to nearest integer
    print(round(total))

if __name__ == '__main__':
    solve()