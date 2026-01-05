import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    A = int(data[0])
    B = int(data[1])

    count = 0

    max_val = A * A + B
    max_square_root = int(math.isqrt(max_val)) + 1

    for square in range(1, max_square_root + 1):
        square_val = square * square
        y = square_val - A * A
        if 1 <= y <= B:
            count += 1

    print(count)

if __name__ == '__main__':
    solve()