import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for Xf in cases:
        max_moves = 0
        current_y = 0
        current_x = 0
        while True:
            # Find the smallest P such that P^2 > current_y and P > current_x
            P = math.isqrt(current_y) + 1
            if P > Xf:
                break
            # Check if P is valid
            if P * P > current_y:
                # Update X and Y
                current_x = P
                current_y += P * P
                max_moves += 1
            else:
                break
        print(max_moves)

if __name__ == '__main__':
    solve()