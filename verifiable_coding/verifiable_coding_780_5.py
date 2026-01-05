import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        remainder = N % M
        if remainder % 2 == 0:
            print("EVEN")
        else:
            print("ODD")