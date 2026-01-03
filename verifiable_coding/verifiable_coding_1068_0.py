import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        if (N % 2 == 0 and M % 2 == 0) or (N % 2 == 1 and M % 2 == 1):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()