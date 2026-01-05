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
        y = 0
        x = 0
        for p in range(1, Xf + 1):
            if p * p > y:
                y += p * p
                x = p
                max_moves += 1
            if x == Xf:
                break
        print(max_moves)

if __name__ == '__main__':
    solve()