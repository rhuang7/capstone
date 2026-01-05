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
        for i in range(1, Xf + 1):
            if i * i > current_y:
                current_y += i * i
                current_x = i
                max_moves += 1
        print(max_moves)

if __name__ == '__main__':
    solve()