import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    idx = 0
    while True:
        n = int(input[idx])
        m = int(input[idx+1])
        x = int(input[idx+2])
        idx += 3
        if n == 0 and m == 0 and x == 0:
            break
        total = 0
        time = 0
        for i in range(1, m+1):
            t = x + (i-1)*n + n
            cost = (t - n) // m
            total += cost
        print(total)

if __name__ == '__main__':
    solve()