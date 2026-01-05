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
    max_square = int(math.isqrt(max_val)) + 1
    
    for square in range(1, max_square + 1):
        s = square * square
        for x in range(1, A + 1):
            y = s - x * x
            if 1 <= y <= B:
                count += 1
    
    print(count)

if __name__ == '__main__':
    solve()