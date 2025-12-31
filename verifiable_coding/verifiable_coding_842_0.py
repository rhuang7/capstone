import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        for j in range(1, K + 1):
            if j % 2 == 1:
                print(f"{j}   {j}")
            else:
                print(f"{j}{j}")
        print()

if __name__ == '__main__':
    solve()