import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        H = int(input[idx])
        X = int(input[idx+1])
        idx += 2
        if H >= X:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()