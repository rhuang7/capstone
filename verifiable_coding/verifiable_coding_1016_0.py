import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        count = 0
        for _ in range(N):
            S = int(input[idx])
            J = int(input[idx + 1])
            idx += 2
            delay = J - S
            if delay > 5:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()