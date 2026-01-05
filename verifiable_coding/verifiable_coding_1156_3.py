import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        if N < 10:
            print("Thanks for helping Chef!")
        else:
            print("-1")

if __name__ == '__main__':
    solve()