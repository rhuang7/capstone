import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for Xf in cases:
        max_moves = 0
        y = 0
        x = 0
        while True:
            # Find the smallest P such that P^2 > y and P > x
            P = math.isqrt(y) + 1
            if P > Xf:
                break
            if P > x:
                # Valid move
                max_moves += 1
                y += P * P
                x = P
            else:
                # Cannot choose P because it's not larger than current x
                break
        print(max_moves)

if __name__ == '__main__':
    solve()