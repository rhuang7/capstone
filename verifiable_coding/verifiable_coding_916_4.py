import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        print(N * M)

if __name__ == '__main__':
    solve()