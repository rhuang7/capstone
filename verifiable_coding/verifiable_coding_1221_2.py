import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Xf_list = list(map(int, data[1:T+1]))
    
    for Xf in Xf_list:
        max_moves = 0
        current_sum = 0
        current_x = 0
        for i in range(1, int(math.isqrt(Xf)) + 2):
            if current_sum + i*i > Xf:
                break
            current_sum += i*i
            max_moves += 1
        print(max_moves)

if __name__ == '__main__':
    solve()