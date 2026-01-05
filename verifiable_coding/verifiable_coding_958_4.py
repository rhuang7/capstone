import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        K = int(data[i])
        for j in range(K):
            if j == 0 or j == K - 1:
                print("*")
            else:
                print(" " * (j - 1) + "*")
        if i < T:
            print()