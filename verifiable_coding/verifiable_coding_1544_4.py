import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        K = int(data[i])
        for j in range(1, K + 1):
            if j % 2 == 1:
                print("*", end="")
            else:
                print("{}", end="")
        print()

if __name__ == '__main__':
    solve()