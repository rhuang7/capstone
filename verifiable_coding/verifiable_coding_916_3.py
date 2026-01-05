import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        print(N * M)

if __name__ == '__main__':
    solve()